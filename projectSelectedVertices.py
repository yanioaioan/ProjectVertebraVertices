'''
orient model along the z axis.
enable backface culling
selected vertices 
execute code
'''

##########################################################################
vertsSelected=cmds.ls( selection=True )#cmds.ls( 'FEMUR*' )
for i in vertsSelected:
    
    if ':' in i:
        print i
        startIndex=int(i.split(':')[0].split('[')[1])
        endIndex=int(i.split(':')[1].split(']')[0])
        print startIndex,endIndex
        for indx in range(startIndex,endIndex+1):
            curPointPosition = cmds.xform( str(i.split('[')[0].split('.')[0])+".pnts["+str(indx)+"]", query=True, translation=True, worldSpace=True )
            
            cmds.polySphere()
            cmds.xform(translation=(curPointPosition[0],curPointPosition[1], -1), scale=(0.1,0.1,0.1) )

    else:
        startIndex=int(i.split('[')[1].split(']')[0])
        print startIndex
        
        curPointPosition = cmds.xform( str(i.split('[')[0].split('.')[0])+".pnts["+str(startIndex)+"]", query=True, translation=True, worldSpace=True )
        print 'curPointPosition',curPointPosition
        cmds.polySphere()
        cmds.xform(translation=(curPointPosition[0],curPointPosition[1], -1), scale=(0.1,0.1,0.1) )








 