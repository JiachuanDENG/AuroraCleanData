from pydub import AudioSegment
import random
import os

path = "../Downloads/tobesegmented2"
files = os.listdir(path)
for fs in files:
    if fs[-3:] != "wav":
        continue
    sound = AudioSegment.from_file(path+"/"+fs,format="wav")
    print "name: %s" % fs
    lenth = len(sound)
    array = []
    for i in range(lenth):
        if sound[i].rms >= 200:
            start = i
            break
    for j in range(lenth-1, -1,-1):
        if sound[j].rms >= 200:
            end = j
            break
    print "start: %d" % start
    print "end: %d" % end
    for k in range(start, end-20, 20):
        print "rms: %d" % sound[k:k+20].rms
        if  sound[k:k+20].rms < 200:
            array.append(k)
    print "array: %s" % array
    ran3 = random.randrange(0,len(array))
    ranleft = array[ran3]
    ranright = array[ran3]+20
    while sound[ranleft].rms < 200:
        ranleft -= 1
    while sound[ranright].rms < 200:
        ranright += 1
    res3 = sound[ranleft-150 : ranright+150] 
    res_len3 = len(res3)
    mid_po = res_len3 / 2
    if res_len3 > 500:
        less = res_len3 - 500
        res_middle = res3[:mid_po - less/2] + res3[mid_po + less/2:]
    elif res_len3 == 500:
        res_middle = res3
    else:
        more = 500 - res_len3
        silence3 = AudioSegment.silent(duration = more)
        res_middle = res3[:mid_po] + silence3 + res3[mid_po:]
    ran1 = random.randrange(50,150)
    ran2 = random.randrange(50,150)
    res1 = sound[start:start+ran1]
    res2 = sound[end-ran2:end]
    res_len1 = len(res1)
    needlen1 = 500 - res_len1
    res_len2 = len(res2)
    needlen2 = 500 - res_len2
    silence1 = AudioSegment.silent(duration=needlen1)
    silence2 = AudioSegment.silent(duration=needlen2)
    res_before = silence1 + res1
    res_after = res2 + silence2
    output1 = res_before.export("./before/"+fs[:-4]+".wav",format = "wav")
    output2 = res_after.export("./after/"+fs[:-4]+".wav",format = "wav")
    output3 = res_middle.export("./middle/"+fs[:-4]+".wav",format = "wav")
    print "channel: %d" % sound.channels
    print "bit: %d" % sound.sample_width
    print "rate: %d" % sound.frame_rate
    print "start_po: %d" % start
    print "random_front_len: %d" % ran1
    print "end_po: %d" % (end-ran2)
    print "random_end_len: %d" % ran2
    print "middle_po: %d" % ran3
    print "random_middle_len: %d" % res_len3
