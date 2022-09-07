#
#
#
import sys
import os
sys.path.append(os.path.abspath('D:\\do\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_sounds\\'))
from sound import *

#twinkle little star
tlsdata = ['c6,c6,g6,g6,a6,a6,g6,xx,f6,f6,e6,e6,d6,d6,c6,xx,g6,g6,f6,f6,e6,e6,d6,xx,g6,g6,f6,f6,e6,e6,d6,xx,c6,c6,g6,g6,a6,a6,g6,xx,f6,f6,e6,e6,d6,d6,c6,xx',
           'cM4,cM4,cM4,cM4,fM4,fM4,cM4,cM4,fM4,fM4,cM4,cM4,gM4,gM4,cM4,cM4,cM4,cM4,fM4,fM4,cM4,cM4,gM4,gM4,cM4,cM4,fM4,fM4,cM4,cM4,gM4,gM4,cM4,cM4,cM4,cM4,fM4,fM4,cM4,cM4,fM4,fM4,cM4,cM4,gM4,gM4,cM4,xxx']

mel = melody(tlsdata[0])
cho = chordsmel(tlsdata[1], 2)
fileout(cho + mel)