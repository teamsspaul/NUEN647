#!/usr/bin/env python3
import Functions as Fun

I=Fun.CPS_Vol_Data('Initial.txt')
F=Fun.CPS_Vol_Data('Final.txt')

#Loop through all the Pairs
for i in range(1,len(I)):
	#Easier variables
	u_I=float(I[i][0]);u_F=float(F[i][0]);o_I=float(I[i][1]);o_F=float(F[i][1]);t1=float(I[i][2]);t2=float(F[i][2])
	V1=float(I[0][0]);oV1=V1*(float(I[0][1])/100);V2=float(F[0][0]);oV2=V2*(float(F[0][1])/100)
	
	#Plot
	fig=Fun.plt.figure(figsize=Fun.FigureSize)
	ax=fig.add_subplot(111)
	label_I="Initial Aqueous Solution"
	label_F="Final Aqueous Solution"
	
	
	(fig,ax)=Fun.plotPDF(ax,'red',u_I,o_I,label_I,fig)
	(fig,ax)=Fun.plotPDF(ax,'blue',u_F,o_F,label_F,fig)
	
	#MDA
	ax=Fun.Calc_N_Plot_MDA(ax,u_I,t1,V1,oV1,u_F,t2,V2,oV2,o_I)
	
	#Legend
	ax=Fun.Legend(ax)
	
	Fun.plt.savefig('GammaEnergy_'+str(i)+'.pdf')

