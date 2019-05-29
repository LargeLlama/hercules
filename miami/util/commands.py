def overlap():
    counter = 0
    while counter < len(start):
        if start[0] > end[0]:
            flash("Start time can't be after end time!")
            return redirect(url_for("create"))
        counter +=1
    tempS = start.sort()
    tempE = start.end()
    if (start != tempS):
        flash("Please sort your tasks in ascending order")
        return redirect(url_for("create"))
    counter = 0
    while counter < len(tempE) -1:
        if end[counter] > start[counter+1]:
            flash("Tasks can't overlap!")
            return redirect(url_for("create"))
        counter +=1
        
        
        
        
    
