from sklearn import tree
x=[[180,80,400],[170,70,50],[160,60,38]]
y=['male','female','female']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
p = clf.predict([[140,70,30]])
print p