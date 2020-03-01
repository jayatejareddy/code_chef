Chef made ***N*** pieces of cakes, numbered them ***1*** through ***N*** and arranged them in a row in this order. There are ***K*** possible types of flavours (numbered ***1*** through ***K***); for each valid ***i***, the ***i-th*** piece of cake has a flavour ***A<sub>i</sub>***.

Chef wants to select a contiguous subsegment of the pieces of cake such that there is at least one flavour which does not occur in that subsegment. Find the maximum possible length of such a subsegment of cakes.

### **Input**

- The first line of the input contains a single integer ***T*** denoting the number of test cases. The description of ***T*** test cases follows.
- The first line of each test case contains two integers ***N*** and ***K***.
- The second line contains N space-separated integers ***A<sub>1</sub>,A<sub>2</sub>,…,A<sub>N</sub>***.

### **Output**

For each test case, print a single line containing one integer ― the maximum length of a valid subsegment.

### **Constraints**

- ***1≤T≤1,000***
- ***1≤N≤10<sup>5</sup>***
- ***2≤K≤10<sup>5</sup>***
- ***1≤A<sub>i</sub>≤K*** for each valid ***i***
- the sum of ***N*** over all test cases does not exceed ***10<sup>6</sup>***

### **Subtasks**

**Subtask #1 (50 points):**

- ***N≤10<sup>3</sup>***
- ***K=2***
- the sum of ***N*** over all test cases does not exceed 104

**Subtask #2 (50 points):** original constraints

### **Example Input**

`2`

`6 2`

`1 1 1 2 2 1`

`5 3`

`1 1 2 2 1`

### **Example Output**

`3`

`5`
