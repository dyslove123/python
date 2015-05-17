import Image
import sys
import neurolab as nl
import matplotlib.pyplot as pl
def convert_to_bw(im):  
    im = im.convert("L")  
    im.save("sample_L.bmp")  
    im = im.point(lambda x: 255 if x > 196 else 0)  
    im = im.convert('1')  
    im.save("sample_1.bmp")  
    return im  

def split(im):  
    assert im.mode == '1'  
    result = []  
    w, h = im.size  
    data = im.load()  
    xs = [1, 10, 19, 28, 37]  
    ys = [1, h-1]  
    for i, x in enumerate(xs):  
        if i + 1 >= len(xs):  
            break  
        for j, y in enumerate(ys):  
            if j + 1 >= len(ys):  
                break  
            box = (x, y, xs[i+1], ys[j+1])  
            t = im.crop(box).copy()  
            box = box + ((i + 1) % 10, )  
#           save_32_32(t, 'num_%d_%d_%d_%d_%d'%box)  
            result.append(t)  
    return result 	

def solve(im):  
	w=im.size[0]
	h=im.size[1]
	box=[1000,1000,0,0]
	for i in range(0,w):
		for j in range(0,h):
			if(im.getpixel((i,j))==0):
				if box[0]>i:
					box[0]=i		
				if box[1]>j:
					box[1]=j 
				if box[2]<i:
					box[2]=i		
				if box[3]<j:
					box[3]=j 
	side=32-(box[2]-box[0])
	box[0]-=side/2;
	box[2]+=side/2+side%2;
	side=32-(box[3]-box[1])
	box[1]-=side/2;
	box[3]+=side/2+side%2;
	box=(box[0],box[1],box[2],box[3])
	t=Image.new('L',(32,32),255)
	t.paste(im,((-box[0]),(-box[1])))
	
	return t


def tran_binary(im):  
	result=[]
	for i in range(0,32,2):
		for j in range(0,32,2):
			a=0
			if(im.getpixel((i,j))==0):
				a=a+1
			if(im.getpixel((i+1,j))==0):
				a=a+1
			if(im.getpixel((i,j+1))==0):
				a=a+1
			if(im.getpixel((i+1,j+1))==0):
				a=a+1	
			result.append(a)
	return result
def tran_to_list(m):
	r=[]
	for i in range(0,10):
		if(m==(i+11)%10):
			r.append(1)
		else:
			r.append(0)
	return r
def tran_to_list_list(m):
	r=[]
	for s in m:
		r.append(tran_to_list(int(s)))
	return r

def get_ans_from_list(m):
	dis=100
	ans=-1
	for i,r in enumerate(m):
		if(1-r<dis):
			ans=(i+11)%10
			dis=1-r
	return ans
def get_ans_from_list_list(m):
	a=''
	for r in m:
		a=a+str(get_ans_from_list(r))
	return a
#root="SAMPLE_BMP.gif"
#im=Image.open(root)
#convert_to_bw(im)
def get_pic_message(im):
	convert_to_bw(im)
	im=Image.open("sample_1.bmp")
	result = split(im)
	message = []
	for i,r in enumerate(result):
		r=solve(r);
		r.save(output+"\\"+str(i)+".bmp");
		message.append(tran_binary(r))
	return message

if __name__ == '__main__':

	output="temp4"
	target="0000"
	begin=40;
	end=50;
	if(len(sys.argv)==3):
		begin=sys.argv[1]
		end=sys.argv[2]
	net = nl.load("train.data")
	for i in range((int)(begin),(int)(end)):
		im=Image.open("temp3\\"+str(i)+".gif")
		message=get_pic_message(im)
		#print net.sim(message)
		print get_ans_from_list_list(net.sim(message))
		
