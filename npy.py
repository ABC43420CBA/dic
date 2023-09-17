import copy#用于实行deepcopy()


def fenbianmoshi(jiaru_l):#看是“英语在前”还是“中文在前”
    '''
    if (ord(jiaru_l[0]) not in range(65,91))&(ord(jiaru_l[0] not in range(97,123)))&(ord(\
        jiaru_l[0])!=32):
        return 0
        '''
    flag=0
    #fengewei=0

    #print(len(jiaru_l))
    #print(jiaru_l)
    #print(ord(jiaru_l[5]))
    
    for i in range(len(jiaru_l)):
        if (jiaru_l[i]==' ')&(i!=len(jiaru_l)-1):

            #print('diyiceng')
            
            if (ord(jiaru_l[i+1]) not in range(65,91))&(ord(jiaru_l[i+1]) not in \
                                                            range(97,123))&(ord(\
        jiaru_l[i+1])!=32):

                #print('dierceng')
                
                if i>0:

                    #print('disanceng')
                    
                    for j in range(0,i):
                        if (ord(jiaru_l[j]) in range(65,91))|(ord(jiaru_l[j])\
                                                              in range(97,123)):
                            flag=1

                            #print(flag)
                            #print('disiceng')
                            
                            break
                    if flag==1:

                        #print('diwuceng')
                        
                        return ['zh',i]

    #print(flag)

    for i in range(1,len(jiaru_l)):
        if (jiaru_l[i]==' ')&(ord(jiaru_l[i-1]) not in range(65,91))&(ord(jiaru_l[i-1]) \
                                                                      not in \
                                                            range(97,123))&(ord(\
        jiaru_l[i-1])!=32):
            for j in range(i,len(jiaru_l)):
                if (ord(jiaru_l[j]) in range(65,91))|(ord(jiaru_l[j]) in range(97,123)):
                    flag=1

                    #print(flag)
                    
                    break
            if flag==1:
                return ['zq',i]

    #print(flag)
    
    if flag==0:
        print('Bad input!')
        return [0,0]


def zh(jiaru_l,i):#中文在后
    Eng=[]
    Chi=[]
    nC=[]
    for j in range(len(jiaru_l)):
        if j<i:
            Eng.append(copy.deepcopy(jiaru_l[j]))
        elif j>i:
            Chi.append(copy.deepcopy(jiaru_l[j]))
    huancun=[Chi[0]]

    #print('huancun:')
    #print(huancun)
    #print('\n')
    #print(Chi)
    
    for k in range(1,len(Chi)):
        if Chi[k]==',':
            nC.append(copy.deepcopy(huancun))
            huancun.clear()
        else:
            huancun.append(copy.deepcopy(Chi[k]))

    #print('test')
    #print(huancun)
    
    if len(huancun)!=0:

        #print("**********************************************************")
        #print(huancun)
        #print(nC)
        #print("********************************************************")
        
        nC.append(copy.deepcopy(huancun))

        #print(nC)
        #print("*********************************************")
        
        huancun.clear()

    #print(nC)
    
    return [Eng,nC]#这是write的存储


def zq(jiaru_l,i):#中文在前
    Eng=[]
    Chi=[]
    nC=[]
    for j in jiaru_l:
        if j>i:
            Eng.append(copy.deepcopy(jiaru_l[j]))
        elif j<i:
            Chi.append(copy.deepcopy(jiaru_l[j]))
    huancun=[Chi[0]]
    for k in range(1,len(Chi)):
        if Chi[k]==',':
            nC.append(copy.deepcopy(huancun))
            huancun.clear()
        else:
            huancun.append(copy.deepcopy(Chi[k]))
    if len(huancun)!=0:
        nC.append(copy.deepcopy(huancun))
        huancun.clear()
    return [Eng,nC]#这是write的结果


def chaxun(s):#实现词典“查询”功能
    zhaodao=0
    sl=list(s)
    for i in range(len(E)):
        if E[i]==sl:
            print(s+' '+Chinese_union(nC[i]))
            zhaodao=1
            break
    for j in range(len(nC)):
        for k in range(len(nC[j])):
            if (nC[j][k])==sl:
                print(s+' '+Chinese_union(nC[j]))
                zhaodao=1
                break
        if zhaodao==1:
            break
    if zhaodao==0:
        print('没有该词。')
        return 0
    else:
        return 1


def Chinese_union(s):#将单个中文字符相连形成一个英语单词or词组的完整释义
    length=len(s)
    l=[]
    for i in range(length):
        l.append('')
        for j in range(len(s[i])):

            #print(s[i][j])
            
            l[i]+=s[i][j]
    for k in range(1,length):
        l[0]+=(','+copy.deepcopy(l[k]))
    return copy.deepcopy(l[0])


def jiayi(write):#对词典中已有词增加中文释义
    nage=0
    for i in range(len(E)):
        if E[i]==write[0]:
            #print(s+' '+','.join(nC[i]))
            #zhaodao=1
            nage=i
            break
    different=[]
    for j in range(len(write[1])):
        differ=1
        for k in range(len(nC[nage])):
            if nC[nage][k]==write[1][j]:
                differ=0
                break
        if differ==1:
            different.append(copy.deepcopy(write[1][j]))
    if len(different)==0:
        print('无可复加！')
    else:
        for q in range(len(different)):
            nC[nage].append(copy.deepcopy(different[q]))
        #print(E[nage]+' '+Chinese_union(different))


def xie_ru(write):#写入到词典中
    if chaxun(''.join(write[0]))==1:
        print('存在该词！')
        if input('是否增加释义？')=='y':
            '''
            for h in range(len(write[1])):
                write[1][h]=''.join(write[1][h])
                '''
            jiayi(write)
    else:
        '''
        fp.seek(2)
        fp.write(''.join(write[0])+' '+Chinese_union(write[1])+'\n')
        print('写入成功！')
        '''
        E.append(copy.deepcopy(write[0]))
        nC.append(copy.deepcopy(write[1]))


def tianjia():#加厚词典的手段之一！
    jiaru=input('加什么？\n\
    （输入英文单词或词组以及中文，中间用一个空格隔开，中文和英文何者在前都可以）')
    jiaru_l=list(jiaru)

    print('jiaru_l',jiaru_l)
    
    pd=fenbianmoshi(jiaru_l)

    #print(pd)
    
    write=0
    if pd[0]=='zh':
        write=zh(jiaru_l,pd[1])
    elif pd[0]=='zq':
        write=zq(jiaru_l,pd[1])
    else:
        print("Wrong format!")
    if write!=0:
        xie_ru(write)


def fl(yiyouci):#将对象读入内存后分割English与Chinese，对其分开存储
    #cache=[]
    E=[]
    C=[]
    nC=[]
    yiyouci_l=[]
    #que=0
    for item in yiyouci:

        #print(item)
        
        yiyouci_l.append(list(copy.deepcopy(item)))

        #print(yiyouci_l)
        
    for j in range(len(yiyouci_l)):
        hefa=0
        w=None
        for k in range(0,len(yiyouci_l[j])):
            if k<len(yiyouci_l[j])-1:
                if (yiyouci_l[j][k]==' ')&(ord(yiyouci_l[j][k+1]) not in range(65,91))&\
                                   (ord(yiyouci_l[j][k+1]) not in \
                                                            range(97,123))&(ord(\
        yiyouci_l[j][k+1])!=32):
                    w=k
                    hefa=1
                    break
        if hefa==0:
            #que+=1
            pass
        else:
            E.append([])
            C.append([])
            #nC=[]#不如改为三层？===============================================算了吧。
            for i in range(len(yiyouci_l[j])):
                if i<w:
                    E[-1].append(copy.deepcopy(yiyouci_l[j][i]))
                if (i>w)&(i<len(yiyouci_l[j])):
                    C[-1].append(copy.deepcopy(yiyouci_l[j][i]))
            nC.append([])
            huancun=[C[-1][0]]
            for p in range(1,len(C[-1])):
                if C[-1][p]==',':
                    nC[-1].append(copy.deepcopy(huancun))
                    huancun.clear()
                else:
                    huancun.append(copy.deepcopy(C[-1][p]))
            if len(huancun)!=0:
                nC[-1].append(copy.deepcopy(huancun))
                huancun.clear()
            
            #E[-1]=''.join(E[-1])
            #C[-1]=''.join(C[-1])
        #cache.clear()
    for n in range(len(nC)):
        for m in range(len(nC[n])):
            if nC[n][m][-1]=='\n':
                nC[n][m].pop(-1)
    return [E,nC]


def xie_yi_xie():#最后：将E与nC以合适的组织形式写入到文件中
    fp=open('cidian.txt','w')
    #fp.seek(0)

    #print(E)
    '''
    print('文件指针位置：')
    print(str(fp.tell()))
    print('E:')
    print(E)
    print('nC:')
    print(nC)
    '''
    #print(E)
    
    for i in range(len(E)):

        #print(nC[i])
        #print('nC:')
        #print(nC)
        
        fp.write(''.join(E[i])+' '+Chinese_union(nC[i]))
        fp.write('\n')
    fp.close()


#main如下***********************************************************************************
cishu=0
tuichu=0
#fp=open('cidian.txt','a+')

#print('Success!')

while (cishu==0):
    fp=open('cidian.txt','a+')

    #print('1943')
    
    fp.seek(0)

    #print('2003')
    
    yiyouci=fp.readlines()

    #print('2004')
    #print(yiyouci)
    
    fenlie=fl(yiyouci)

    #print('i')
    
    E=fenlie[0]
    nC=fenlie[1]
    fp.seek(0)
    #print(fp.tell())
    '''
    if cishu!=0:
        print('指针当前位置：'+str(fp.tell()))
        if input('指针归位吗？')=='y':
            fp.seek(0)
            '''
    caozuo=input('干什么？\n添加还是查询还是退出？')
    cishu+=1
    if caozuo=='退出':
        print('Goodbye!')
        tuichu=1
        break
        #fp.close()
    else:
        if caozuo=='添加':
            tianjia()
            #fp.close()
        elif caozuo=='查询':
            chaxun(input('查什么？哪个？（输入英文单词或词组）'))
            #fp.close()
        else :
            print('Wrong input!')
            #fp.close()
    fp.close()
    xie_yi_xie()
    #print('已退出！可查看词典文件！')
    #fp.close()
if tuichu==0:
    while (input('Continue?（是则输入y，否则输入其他字符以实现退出）')=='y'):
        fp=open('cidian.txt','a+')
        fp.seek(0)
        yiyouci=fp.readlines()
        fenlie=fl(yiyouci)
        E=fenlie[0]
        nC=fenlie[1]
        fp.seek(0)
        #print(fp.tell())
        '''
        if cishu!=0:
            print('指针当前位置：'+str(fp.tell()))
            if input('指针归位吗？')=='y':
                fp.seek(0)
                '''
        caozuo=input('干什么？\n添加还是查询还是退出？')
        cishu+=1
        if caozuo=='退出':
            print('Goodbye!')
            break
            #fp.close()
        else:
            if caozuo=='添加':
                tianjia()
                #fp.close()
            elif caozuo=='查询':
                chaxun(input('查什么？哪个？（输入英文单词或词组）'))
                #fp.close()
            else :
                print('Wrong input!')
                #fp.close()
        fp.close()
        xie_yi_xie()
        #print('已退出！可查看词典文件！')
        #fp.close()
print('已退出！可查看词典文件！')


#感觉这有点像个rubbish program啊……    (lll￢ω￢)
