# Traffic Rule Violation Ranking System

<p align="center">
<img width="700" alt="Screenshot 2021-06-10 at 22 56 54" src="https://user-images.githubusercontent.com/46227224/121570102-29532f80-ca3f-11eb-9280-8f9cfc6b8de0.png">
</p>

## Introduction

1. In the current scenario, the key issue faced by commuters while travelling is to deal with the inefficiency and discrepancy in the traffic system and the people involved in managing the same. 
2. On being caught by the police, the commuter must submit his driving license, RC Book and/or other vehicle documents for verification. In case the commuter forgets/misplaces the documents, he/she is unnecessarily fined. 
3. In case a vehicle is booked for any traffic violations, the details are uploaded onto a website. The owner is not updated with this information. If he fails to check this website regularly, he may not be aware of any pending traffic violations on his vehicles. 
4. In case a vehicle is stolen, the owner must contact the nearest police station. The process to lodge a complaint and subsequent response is slow and inefficient. 

## Detailed Diagram

<p align="center">
<img width="700" alt="Screenshot 2021-06-10 at 22 56 54" src="https://user-images.githubusercontent.com/46227224/121570314-60294580-ca3f-11eb-8ad8-5c73451b23c6.png">
</p>


## Modules

1. RTO module architecture
2. Police module architecture
3. General user module architecture

### RTO Module Architecture
<p align="center">
<img width="300" alt="Screenshot 2021-06-10 at 22 56 54" src="https://user-images.githubusercontent.com/46227224/121570641-ac748580-ca3f-11eb-9c2e-b54c1c539659.png">
</p>

This module is explicitly intended for the RTO director and it comprises of data's identified with the client permit and vehicle. This data will be put away in the database.

### Police Module Architecture

<p align="center">
<img width="300" alt="Screenshot 2021-06-10 at 22 56 54" src="https://user-images.githubusercontent.com/46227224/121570774-d168f880-ca3f-11eb-85c5-ffc88cab74c8.png">
</p>

This module principally centers around giving the data just to the police. It comprises of vehicle data and permit information's. It too creates the fine.
Signs in through the application using the user id provided to him as authentication.

1. Can enter a vehicle number to view the owner’s or vehicle’s documents and previous unpaid offences.
2. Can report any offences committed by the driver.
3. Receives reports about vehicles stolen under his jurisdiction/working location.

![image](https://user-images.githubusercontent.com/46227224/121570801-d9289d00-ca3f-11eb-8bb6-bc89b3605165.png)


### General user architecture

<p align="center">
<img width="300" alt="Screenshot 2021-06-10 at 22 56 54" src="https://user-images.githubusercontent.com/46227224/121570934-02e1c400-ca40-11eb-8861-37b28c851b48.png">
</p>

1. Signs in through the application using the user id provided for authentication.
2. Can view all the latest documents such as driving license, owned vehicle details, RC, latest emission test certificate, insurance copy, etc. in their account.
3. Can report stolen vehicle to notify the nearest police.
4. Can check/pay any unpaid offences on his vehicle.

## Problems

1. The proposed system overcomes these issues in the current scenario by implementing a web server which uses a database to store, update and access the above mentioned documents with a user-friendly application, tailored to the needs of the appropriate users. 
2. The application also allows users to report a stolen vehicle and check unpaid offences on his vehicle, all in the click of a button. 
3. The application for the police allows him to review earlier driving offences by the rider and also report any current offence committed by him. 


## Solution

1. Proposed project is an approach to solve such problems that is by storing all the information related to vehicle and driver at database by RTO administrator.
2. A application is provided to traffic police to retrieve vehicle and license information and all the challans will notify the commuter through message or email. 
3. A stolen vehicle report will be viewed by the police and the police can update the status of the stolen vehicle through the application which will notify the user. This approach is also useful to penalize the offenders, who violate the traffic rules.
4. The police’s account can generates a digital receipt avoiding any kind of unwanted tampering with the process. 






