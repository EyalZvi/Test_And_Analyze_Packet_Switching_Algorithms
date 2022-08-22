# Test And Analyze Packet Switching Algorithms

**With the ongoing increase of users online, one of the major factors of network efficiency is congestion control**.

Many service providers try to solve this problem by using load balancing algorithms when the main goal is to minimize service time and reduce congestion in each server individually

In this Mininet project we will simulate and compare different scheduling algorithms in order to determine which of the algorithms tested is optimal for each scenario.

# Test Cases:

**1) Topology 1**: 3 Clients vs. 3 Servers - All servers with equal service times:



![image](https://user-images.githubusercontent.com/92316457/185902828-b7ac0242-f850-4b9a-b4b2-33afce5b8190.png)

**2) Topology 1**: 3 Clients vs. 3 Servers - All servers with differnet service times:



![image](https://user-images.githubusercontent.com/92316457/185903023-571d4603-424b-49b7-a249-0007f099c9da.png)


**3) Topology 2**: 6 Clients vs. 3 Servers - All servers with equal service times:


![image](https://user-images.githubusercontent.com/92316457/185903409-3bb671b1-52d0-48e7-ada4-a6590913ff4c.png)

**3) Topology 2**: 6 Clients vs. 3 Servers - All servers with different service times:


![image](https://user-images.githubusercontent.com/92316457/185903483-33e2ca77-9a8d-4e01-a760-5f4030e4b240.png)

# Results and Conclusions:

**THE RESULTS OF ALL FOUR TOPOLOGIES ARE SHOWN IN GRAPH FORM IN THE PPTX FILE**

**According to our model and simulation results:**

WFQ is optimal for servers with different service times given properly assigned weights.

Given identical service times the optimal algorithm is RR.

As the number of clients increase the Random algorithm shows more efficiency and becomes the 2nd optimal choice.

We conclude that when the topology and weights are known it is most efficient using RR or WFQ according to the ratio between server weights.
Otherwise, using the Random algorithm can result in higher efficiency than choosing one of the other algorithms.



