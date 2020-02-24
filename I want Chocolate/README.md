**<p align=center>Give me Chocolate</p>**

Anushka wants to buy chocolates.there are many chocolates in front of her, tagged with their prices.
Anushka has only a certain amount to spend, and she wants to maximize the number of chocolates she buys with this money.

Given a list of prices and an amount to spend, what is the maximum number of chocolates Anushka can buy?

**For example** ,</br>
if prices =[1,2,3,4] and Anushka has k=7 to spend, she can buy items [1,2,3] for 6 , or [3,4] for 7 units of currency. she would choose the first group of 3 items.

**Input Format**</br>
The first line contains two integers, n and k , the number of priced chocolates and the amount Anushka has to spend.
The next line contains n space-separated integers prices[i]

**Constraints**</br>
1\&lt;= n \&lt;= 105
1\&lt;= k \&lt;= 109
1\&lt;= prices[i] \&lt;= 109

A chocolate can&#39;t be bought multiple times.

**Output Format**</br>
An integer that denotes the maximum number of chocolates Anushka can buy for her.

**Sample Input**</br>
7 50
1 12 5 111 200 1000 10

**Sample Output**</br>
4

**Explanation**</br>
she can buy only 4 chocolatess at most. These chocolates have the following prices: 1, 12, 5, 10.
