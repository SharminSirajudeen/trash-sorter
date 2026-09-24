"""Train a fresh-vs-spoiled produce classifier and export it in Teachable
Machine format so FreshEye loads it unchanged.

Normalization matches what the TM image library does in-browser: (x/127 - 1).
"""
import os, sys, types, json, glob, datetime, random
sys.modules.setdefault('tensorflow_decision_forests', types.ModuleType('tensorflow_decision_forests'))
import numpy as np
from PIL import Image
import tensorflow as tf
import tensorflowjs as tfjs

SP='/tmp/claude-0/-home-user-trash-sorter/43c6b523-272a-51b6-a829-7007aa59f5f9/scratchpad'
SRC=SP+'/fruitds/Datasets/train'
OUT=SP+'/model_fresh_out'
IMG=224
CAP=1200                      # per class, keeps memory ~1.5GB
random.seed(1); np.random.seed(1); tf.random.set_seed(1)

FOLDER2CLASS={'freshapples':'fresh','freshbanana':'fresh','freshoranges':'fresh',
              'rottenapples':'spoiled','rottenbanana':'spoiled','rottenoranges':'spoiled'}
LABELS=['fresh','spoiled']
L2I={l:i for i,l in enumerate(LABELS)}

def center_square_resize(im):
    w,h=im.size; s=min(w,h)
    im=im.crop(((w-s)//2,(h-s)//2,(w+s)//2,(h+s)//2))
    return im.resize((IMG,IMG), Image.BILINEAR)

# gather a balanced, shuffled sample
by_class={l:[] for l in LABELS}
for folder,cls in FOLDER2CLASS.items():
    by_class[cls]+= glob.glob(os.path.join(SRC,folder,'*'))
paths=[]
for cls,fs in by_class.items():
    random.shuffle(fs)
    paths += [(p,L2I[cls]) for p in fs[:CAP]]
random.shuffle(paths)
print("sampled:", {l: sum(1 for _,y in paths if y==L2I[l]) for l in LABELS})

X=np.zeros((len(paths),IMG,IMG,3),dtype=np.float32)
y=np.zeros((len(paths),),dtype=np.int64)
ok=0
for p,lab in paths:
    try:
        im=center_square_resize(Image.open(p).convert('RGB'))
    except Exception:
        continue
    X[ok]=np.asarray(im,dtype=np.float32)/127.0-1.0
    y[ok]=lab; ok+=1
X=X[:ok]; y=y[:ok]
print("loaded:", X.shape, "counts:", np.bincount(y,minlength=len(LABELS)))

n=len(X); nval=int(n*0.15)
Xval,yval=X[:nval],y[:nval]; Xtr,ytr=X[nval:],y[nval:]
print(f"train={len(Xtr)} val={len(Xval)}")

base=tf.keras.applications.MobileNetV2(input_shape=(IMG,IMG,3),include_top=False,
                                       weights='imagenet',pooling='avg')
base.trainable=False
print("extracting embeddings...")
Etr=base.predict(Xtr,batch_size=32,verbose=1)
Eval=base.predict(Xval,batch_size=32,verbose=1)

emb=tf.keras.Input(shape=(Etr.shape[1],))
h=tf.keras.layers.Dense(128,activation='relu',name='head_dense1')(emb)
h=tf.keras.layers.Dropout(0.3)(h)
out=tf.keras.layers.Dense(len(LABELS),activation='softmax',name='head_out')(h)
head=tf.keras.Model(emb,out)
head.compile(optimizer=tf.keras.optimizers.Adam(1e-3),
             loss='sparse_categorical_crossentropy',metrics=['accuracy'])
head.fit(Etr,ytr,validation_data=(Eval,yval),epochs=40,batch_size=32,verbose=2,
         callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_accuracy',patience=8,
                                                     restore_best_weights=True)])
vloss,vacc=head.evaluate(Eval,yval,verbose=0)
print(f"\nVALIDATION ACCURACY: {vacc:.3f}")
pred=head.predict(Eval,verbose=0).argmax(1)
for i,l in enumerate(LABELS):
    m=yval==i
    print(f"  {l:8s} n={int(m.sum()):4d} acc={(pred[m]==i).mean():.3f}")

combined=tf.keras.Model(base.input, head(base.output))
os.makedirs(OUT,exist_ok=True)
tfjs.converters.save_keras_model(combined,OUT)
json.dump({"tfjsVersion":tf.__version__,"tmVersion":"2.4.7","packageVersion":"0.8.5",
           "packageName":"@teachablemachine/image",
           "timeStamp":datetime.datetime.utcnow().isoformat()+"Z","userMetadata":{},
           "modelName":"fresheye-baseline","labels":LABELS,"imageSize":IMG},
          open(os.path.join(OUT,'metadata.json'),'w'),indent=2)

vd=OUT+'/_valset'; os.makedirs(vd,exist_ok=True)
truth=[]
for i in range(min(40,len(Xval))):
    arr=((Xval[i]+1.0)*127.0).clip(0,255).astype(np.uint8)
    Image.fromarray(arr).save(f"{vd}/{i}.png")
    truth.append({"file":f"{i}.png","label":LABELS[int(yval[i])]})
json.dump(truth,open(vd+'/truth.json','w'))
print("\nExported to",OUT,"| files:",sorted(os.listdir(OUT)))
