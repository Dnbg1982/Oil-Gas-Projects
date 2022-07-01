%clear
load welllog_new.mat
data(:,1:5)=welllog{:,2:6};
data(:,6:8)=welllog{:,9:11};
data(:,9:10)=welllog{:,14:15};
data(:,11)=welllog{:,18};
data(:,12)=welllog{:,19};
data(:,13)=welllog{:,20};
% 1twt 2tvdss 3inline 4xline 5gamma 6nphi 7cal 8rhob 9vp 10vs 11diff_log
% 12vel 13formation
%vel vp gamma diff_log vs rhob  

% data_vs=data;
% data_vs(any(isnan(data_vs(:,10)), 2),:)=[];
% data_vs_1=data_vs(:,9);
% data_vs_2=data_vs(:,10);
%data=single(data);
% index2=(find(data(:,13)==2));
% data2=data(index2,:);
% index3=(find(data(:,13)==3));
% data3=data(index3,:);
% index4=(find(data(:,13)==4));
% data4=data(index4,:);
% index5=(find(data(:,13)==5));
% data5=data(index5,:);
for i=1:size(data,2)
    miss(i)=sum(isnan(data(:,i)))/size(data,1)*100.;
end
load data_vel_input
per_vel=prctile(data_vel_input{:,12},[2 98],'all');
data_vel=data_vel_input;
idx=data_vel{:,12}>=4500;
data_vel(idx,:)=[];
idx=data_vel{:,12}<=1200;
data_vel(idx,:)=[];
% data_vel=data_vel{data_vel{:,12}<=3000};
% data_vel=data_vel{data_vel{:,12}>=1200};
%%
figure
subplot(13,1,1);
plot(data_vel_input{:,1});
set(gca,'xtick',[]);
subplot(13,1,2);
plot(data_vel_input{:,2});
set(gca,'xtick',[]);
subplot(13,1,3);
plot(data_vel_input{:,3});
set(gca,'xtick',[]);
subplot(13,1,4);
plot(data_vel_input{:,4});
set(gca,'xticklabel',[]);
subplot(13,1,5);
plot(data_vel_input{:,5});
set(gca,'xticklabel',[]);
subplot(13,1,6);
plot(data_vel_input{:,6});
set(gca,'xticklabel',[]);
subplot(13,1,7);
plot(data_vel_input{:,7});
set(gca,'xticklabel',[]);
subplot(13,1,8);
plot(data_vel_input{:,8});
set(gca,'xticklabel',[]);
subplot(13,1,9);
plot(data_vel_input{:,9});
set(gca,'xticklabel',[]);
subplot(13,1,10);
plot(data_vel_input{:,10});
set(gca,'xticklabel',[]);
subplot(13,1,11);
plot(data_vel_input{:,11});
set(gca,'xticklabel',[]);
xlim([0 14000]);
subplot(13,1,12);
plot(data_vel_input{:,12});
set(gca,'xticklabel',[]);
subplot(13,1,13);
plot(data_vel_input{:,13});
set(gca,'xticklabel',[]);
%%
load model_vel
% data_vel_input(:,1:4)=data(:,1:4);
% data_vel_input(:,5)=data(:,13);
%data_vel_input=welllog;
data_new=data_vel_input;
data_fill_vel=trainedModel_vel.predictFcn(data_vel_input);
index_vel= isnan(data_vel_input{:,12});
for i=1:size(data_vel_input,1)
    if (data_vel_input{i,12}>=4500) | (data_vel_input{i,12}<=1200) | (index_vel(i)==1)      
       data_new{i,12}=data_fill_vel(i);
    end
end
%%
figure
% plot(data(:,12));
plot(data_new{:,12});
 hold on
plot(data(:,12),'--');
ylim([1000  8000]);


%figure
% plot(data(:,12));
 %hold on

ylim([1000  8000]);
legend('Predicted','True');
%%
%%%%5gamma
data_gamma=data_new;
% idx=data_gamma{:,5}>=160;
% data_gamma(idx,:)=[];
% idx=data_gamma{:,5}<=1;
% data_gamma(idx,:)=[];
 load model_gamma
data_new_1=data_new;
data_fill_gamma=trainedModel_gamma.predictFcn(data_new);
index_gamma= isnan(data_new{:,5});
for i=1:size(data_new,1)
    if (data_new{i,5}>=160) | (data_new{i,5}<=1) | (index_gamma(i)==1)      
       data_new_1{i,5}=data_fill_gamma(i);
    end
end

%%
figure
% plot(data(:,12));
% hold on
plot(data_new_1{:,5});
ylim([0  180]);
%figure
% plot(data(:,12)); 
hold on
plot(data_new{:,5},'--');
ylim([0 180]);
legend('Pred','True');

%%
%%%9vp
data_vp=data_new_1;
% idx=isnan(data_vp{:,9});
% data_vp{idx,:}=0.0;
% idx=data_vp{:,9}>=6500;
% data_vp(idx,:)=[];
% idx=data_vp{:,9}<=1500;
% data_vp(idx,:)=[];
 load model_vp
data_new_2=data_new_1;
data_fill_vp=trainedModel_vp.predictFcn(data_new_1);
index_vp= isnan(data_new_1{:,9});
for i=1:size(data_new_1,1)
    if (data_new_1{i,9}>=6500) | (data_new_1{i,9}<=1500) | (index_vp(i)==1)      
       data_new_2{i,9}=data_fill_vp(i);
    end
end
%%
figure
% plot(data(:,12));
% hold on
plot(data_new_2{:,9});
ylim([1000 7000]);
%legend('True');
%figure
hold on
plot(data_new{:,9},'--');
ylim([1000 7000]);
legend('Pred','True');
%%
%%%11 difflog
data_difflog=data_new_2;
% idx=isnan(data_difflog{:,11});
% data_difflog{idx,:}=50.;
% idx=data_difflog{:,11}>=2.0;
% data_difflog(idx,:)=[];
% idx=data_difflog{:,11}<=-2.0;
% data_difflog(idx,:)=[];
 load model_difflog
data_new_3=data_new_2;
data_fill_difflog=trainedModel_difflog.predictFcn(data_new_2);
index_difflog= isnan(data_new_2{:,11});
for i=1:size(data_new_2,1)
    if (data_new_2{i,11}>=2.0) | (data_new_2{i,11}<=-2.0) | (index_difflog(i)==1)      
       data_new_3{i,11}=data_fill_difflog(i);
    end
end
%%
figure
% plot(data(:,12));
% hold on
plot(data_new_3{:,11});
%plot(data_fill_difflog+1);
ylim([-2.0 3.0]);
%legend('True');
%figure
hold on
plot(data_new{:,11},'--');
ylim([-2.0 3.0]);
legend('Pred','True');

%%
%%%7 cal
data_cal=data_new_3;
% idx=isnan(data_cal{:,7});
% data_cal{idx,:}=50.;
% idx=data_cal{:,7}>=10.0;
% data_cal(idx,:)=[];
% idx=data_cal{:,7}<=2.5;
% data_cal(idx,:)=[];
 load model_cal
data_new_4=data_new_3;
data_fill_cal=trainedModel_cal.predictFcn(data_new_3);
index_cal= isnan(data_new_3{:,7});
for i=1:size(data_new_3,1)
    if (data_new_3{i,7}>=10.0) | (data_new_3{i,7}<=2.5) | (index_cal(i)==1)      
       data_new_4{i,7}=data_fill_cal(i);
    end
end
%%
figure
% plot(data(:,12));
% hold on
plot(data_new_4{:,7});
%plot(data_fill_difflog+1);
ylim([2 12]);
%legend('True');
%figure
hold on
plot(data_new{:,7},'--');
ylim([2 12]);
legend('Pred','True');

%%
%%%nphi
data_nphi=data_new_4;
% idx=isnan(data_nphi{:,6});
% data_nphi{idx,:}=100.;
% idx=data_nphi{:,6}>=60;
% data_nphi(idx,:)=[];
% idx=data_nphi{:,6}<=1;
% data_nphi(idx,:)=[];
load model_nphi
data_new_5=data_new_4;
data_fill_nphi=trainedModel_nphi.predictFcn(data_new_4);
index_nphi= isnan(data_new_4{:,6});
for i=1:size(data_new_4,1)
    if (data_new_4{i,6}>=60.0) | (data_new_4{i,6}<=1) | (index_nphi(i)==1)      
       data_new_5{i,6}=data_fill_nphi(i);
    end
end
%%
figure
plot(data_new_5{:,6});
%plot(data_fill_difflog+1);
ylim([0 80]);
hold on
plot(data_new{:,6},'--');
ylim([0 80]);
legend('Pred','True');

%%
%%%
data_rhob=data_new_5;
% idx=isnan(data_rhob{:,8});
% data_rhob{idx,:}=100.;
% idx=data_rhob{:,8}>=4;
% data_rhob(idx,:)=[];
% idx=data_rhob{:,8}<=1.8;
% data_rhob(idx,:)=[];
load model_rhob1
data_new_6=data_new_5;
data_fill_rhob=trainedModel_rhob1.predictFcn(data_new_5);
%data_fill_rhob=trainedModel_rhob2.predictFcn(data_new_5);
index_rhob= isnan(data_new_5{:,8});
for i=1:size(data_new_5,1)
    if (data_new_5{i,8}>=4.0) | (data_new_5{i,8}<=1.8) | (index_rhob(i)==1)      
       data_new_6{i,8}=data_fill_rhob(i);
    end
end
%%
figure
%plot(data_new_6{:,8});
plot(data_fill_rhob);
ylim([1 4]);
hold on
plot(data_new{:,8},'--');
ylim([1 4]);
legend('Pred','True');

%%
%%%
data_vs=data_new_6;
% idx=isnan(data_vs{:,10});
% data_vs{idx,:}=50.;
% idx=data_vs{:,10}>=5000;
% data_vs(idx,:)=[];
% idx=data_vs{:,10}<=800;
% data_vs(idx,:)=[];
load model_vs1
load model_vs2
data_new_7=data_new_6;
data_fill_vs=trainedModel_vs1.predictFcn(data_new_6);
%data_fill_vs=trainedModel_vs2.predictFcn(data_new_6);
index_vs= isnan(data_new_6{:,10});
for i=1:size(data_new_6,1)
    if (data_new_6{i,10}>=5000.0) | (data_new_6{i,10}<=800) | (index_vs(i)==1)      
       data_new_7{i,10}=data_fill_vs(i);
    end
end
figure
%plot(data_new_7{:,10});
plot(data_fill_vs);
ylim([500 4000]);
hold on
plot(data_new{:,10});
ylim([500 4000]);
legend('Pred','True');
%%
data_fill=data_new_7;



%%

figure
subplot(13,1,1);
plot(data_new_7{:,1});
set(gca,'xtick',[]);
subplot(13,1,2);
plot(data_new_7{:,2});
set(gca,'xtick',[]);
subplot(13,1,3);
plot(data_new_7{:,3});
set(gca,'xtick',[]);
subplot(13,1,4);
plot(data_new_7{:,4});
set(gca,'xticklabel',[]);
subplot(13,1,5);
plot(data_new_7{:,5});
set(gca,'xticklabel',[]);
subplot(13,1,6);
plot(data_new_7{:,6});
set(gca,'xticklabel',[]);
subplot(13,1,7);
plot(data_new_7{:,7});
set(gca,'xticklabel',[]);
subplot(13,1,8);
plot(data_new_7{:,8});
set(gca,'xticklabel',[]);
subplot(13,1,9);
plot(data_new_7{:,9});
set(gca,'xticklabel',[]);
subplot(13,1,10);
plot(data_new_7{:,10});
set(gca,'xticklabel',[]);
subplot(13,1,11);
plot(data_new_7{:,11});
set(gca,'xticklabel',[]);
xlim([0 14000]);
subplot(13,1,12);
plot(data_new_7{:,12});
set(gca,'xticklabel',[]);
subplot(13,1,13);
plot(data_new_7{:,13});
set(gca,'xticklabel',[]);








%%
%%%10vs
data_vs=data_new_4;
% idx=isnan(data_vs{:,10});
% data_vs{idx,:}=50.;
% idx=data_vs{:,10}>=5000;
% data_vs(idx,:)=[];
% idx=data_vs{:,10}<=800;
% data_vs(idx,:)=[];

load model_vs
data_new_5=data_new_4;
data_fill_vs=trainedModel_vs.predictFcn(data_new_4);
index_vs= isnan(data_new_4{:,10});
for i=1:size(data_new_4,1)
    if (data_new_4{i,10}>=5000.0) | (data_new_4{i,10}<=800) | (index_vs(i)==1)      
       data_new_5{i,10}=data_fill_vs(i);
    end
end
figure
% plot(data(:,12));
% hold on
plot(data_new_5{:,10});
%plot(data_fill_difflog+1);
ylim([500 4000]);
%legend('True');
%figure
hold on
plot(data_new{:,10});
ylim([500 4000]);
legend('Pred','True');
%%
%%%6nphi
data_nphi=data_new_4;

% data2_vs_new=data2(~isnan(data2(:,10)),:);
% data2_vs_new_vp=data2_vs_new(:,9);
% data2_vs_new_vs=data2_vs_new(:,10);



















%%
% figure
% plot(data2(:,1),data2(:,5));
% hold on
% plot(data2(:,1),data2(:,6));
% hold on
% plot(data2(:,1),data2(:,7));
% hold on
% plot(data2(:,1),data2(:,8));
% hold on
% plot(data2(:,1),data2(:,9));
% hold on
% plot(data2(:,1),data2(:,10));
% hold on
% plot(data2(:,1),data2(:,11));
% hold on
% plot(data2(:,1),data2(:,12));
% 
% legend('1','2','3','4','5','6','7','8');
% 

%%


%%%%%

% vpvs2=data2(:,13:14);vpvs2(any(isnan(vpvs2(:,2)), 2),:)=[];
% vpvs2_1=vpvs2(:,1);vpvs2_2=vpvs2(:,2);
% vpvs3=data3(:,13:14);vpvs3(any(isnan(vpvs3(:,2)), 2),:)=[];
% vpvs3_1=vpvs3(:,1);vpvs3_2=vpvs3(:,2);
% vpvs4=data4(:,13:14);vpvs4(any(isnan(vpvs4(:,2)), 2),:)=[];
% vpvs4_1=vpvs4(:,1);vpvs4_2=vpvs4(:,2);
% vpvs5=data5(:,13:14);vpvs5(any(isnan(vpvs5(:,2)), 2),:)=[];
% vpvs5_1=vpvs5(:,1);vpvs5_2=vpvs5(:,2);
% 
% %%
% 
% data_den=data;
% data_den(any(isnan(data_den(:,10)), 2),:)=[];
% 
% data_den_3(:,1)=0.31.*data_den(:,13).^0.25;
% 
% data_den_1=data_den(:,10);
% data_den_2=data_den(:,13);
% data_den_1=data_den_1-mean(data_den_1);
% data_den_3=data_den_3-nanmean(data_den_3);
% 
% figure
% plot(data_den_1);
% hold on
% plot(data_den_3);
% legend('True','Gardner');
% 
% vpden2(:,1)=data2(:,10); vpden2(:,2)=data2(:,13);  vpden2(any(isnan(vpden2(:,1)), 2),:)=[];
% vpden2_1=vpden2(:,1);vpden2_2=vpden2(:,2);
% vpden3(:,1)=data3(:,10); vpden3(:,2)=data3(:,13);  vpden3(any(isnan(vpden3(:,1)), 2),:)=[];
% vpden3_1=vpden3(:,1);vpden3_2=vpden3(:,2);
% vpden4(:,1)=data4(:,10); vpden4(:,2)=data4(:,13);  vpden4(any(isnan(vpden4(:,1)), 2),:)=[];
% vpden4_1=vpden4(:,1);vpden4_2=vpden4(:,2);
% vpden5(:,1)=data5(:,10); vpden5(:,2)=data5(:,13);  vpden5(any(isnan(vpden5(:,1)), 2),:)=[];
% vpden5_1=vpden5(:,1);vpden5_2=vpden5(:,2);
% 
% data2(any(isnan(data2(:,14)), 2),:)=[];
% data3(any(isnan(data3(:,14)), 2),:)=[];
% data4(any(isnan(data4(:,14)), 2),:)=[];
% data5(any(isnan(data5(:,14)), 2),:)=[];