#Build the neuron network
fnn = buildNetwork(ds_train.indim, 10, ds_train.outdim, outclass=SoftmaxLayer)

#setup the backpropagation trainer
trainer = BackpropTrainer(fnn, dataset=ds_train, momentum=0.1, verbose=True, learningrate=0.01)

#traint the network and save error 
errortrain=np.array(())
errortest=np.array(())
t=np.array(())
for i in range(50):
    trainer.train()
    result_train = percentError(trainer.testOnClassData(),
                         ds_train['class'] )
    result_test = percentError(trainer.testOnClassData(
       dataset=ds_test ), ds_test['class'] )
    errortrain=np.append(errortrain,result_train)
    errortest=np.append(errortest,result_test)
    t=np.append(t,i)

#plot the error    
pl.figure(figsize=(10,10))
pl.plot(t,errortrain)
pl.plot(t,errortest)
plt.xlabel('epoch')
plt.ylabel('error')
plt.title('NN training test error')
plt.legend(['train error', 'test error'], loc='upper left')
pl.show()