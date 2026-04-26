# Log Analyzer Project

##  Steps to Run the Program

1. Install Python  in pycharm or vscode (i have done on both )
2. Install matplotlib:
   pip install matplotlib  (imp otherwise code will not run )
3. Keep these files in same folder:

   * log_analyzer.py
   * logs.txt
4. Open terminal in that folder
5. Run:
   python log_analyzer.py

Output will be shown and graph will be shown 

***

##  Logic

I started by testing small parts like reading the file and counting logs.
After that, I combined everything into one program.

The program reads the file line by line.

It does:

* Count total logs
* Separate logs into ERROR, INFO, WARNING
* Find booking failures using "driver unavailable"
* Find empty runs using "No return load"

I used: (which i revised  first )

* Counter → for top errors and routes
* Regex → to extract orderId and route
* Set → to store unique failed order IDs



## Enhancement

I added a graph using matplotlib.

This shows:

* ERROR count
* INFO count
* WARNING count

It makes the output easier to understand.



## Screenshots

* Testing code ![counting](screenshots/counting.png)
               ![types](screenshots/types.png)
               ![failure](screenshots/failure.png)
               ![noreturn](screenshots/noreturn.png)  
* Final output ![Output](screenshots/output.png)
* Graph ![graph](screenshots/graph.png)



## Assumptions

* Log format is same everywhere
* ERROR / INFO / WARNING always exist
* "driver unavailable" = booking failure
* "No return load" = empty truck
* Routes are like Delhi-Mumbai
* orderId format is orderId=XXXX



## Limitations

* Command line input not added
* Large file handling is basic

****************************

#  Conclusion

This project helped me understand log analysis and how to extract useful data using Python.