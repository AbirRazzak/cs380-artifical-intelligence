# Written Problems

### A. Current Events

#### Write a paragraph summarizing the main points of the article.

Basically, Facebook goes down for an entire day due to a human error in the code. The issue was fixed quickly, but the reason for the service being down for a whole 24 hours is because Facebook has so many systems in place that calling a full reboot can take several hours. Facebook deploys a lot of machine learning to collect data on its users and intelligently present ads to them to purchase items from partners. It also uses machine learning algorithms to show favorable content first on one's feed to keep them on the site longer.

#### In a separate paragraph, you should discuss the societal impact of the technologies discussed in the article

Facebook is seen as the frontier of social movements of the internet age. Being able to connect and stay up to date with friends and family from all around the globe is such an amazing phenomenon. But, it's not without its drawbacks. In the end, the website is still run by a company, and as a company does, they want to make money. And lots of it at that. With all the information that's being voluntarily collected through this social media platform (and Instagram as well), this information can be collected and sold off to other companies to target you and create a very complete profile of you. Europe is leading the charge on trying to establish a safe internet environment, with laws that prevent collecting data in certain situations. I think in 10 years, that will be the direction that we will ultimately have to go in, to prevent these malicious big companies from collecting all of our data and breaching our internet privacy.

#### Write a description of 1-2 sentences that informs a potential reader what the article contains.

Human error caused Facebook services to go down for 24 hours. Fixing the bug wasn't the issue, rebooting all their services were.

### B. Production Systems

#### a. Losing Your Marbles

- Knowledge Base: Baskets exists, and there are 3 them. Marbles exist within those baskets.

- Rules

  - Precondition: If the baskets do not have the same amount of marbles

  - Action: Then choose a basket to double and remove half the amount from another basket

- Initial State: There are 3 baskets with a X amount of marbles in basket 1, Y amount in basket 2, and Z amount in basket 3.

- State Representation:
```
A B C
```
Where A, B, and C represent a basket with a certain number of marbles. Goal condition is A = B = C

- Goal/Termination Condition: When all 3 baskets have the same number of marbles

#### b. The N Queens

- Knowledge Base: There is an chess board, and queens exist on that board. -->

- Rules

  - Precondition: If a queen can be killed by another queen on the board

  - Action: Then place the queen somewhere else on the board

- Initial State: There is a board that has a dimension of NxN and there are Y amount of queens to be placed on the board.

- State Representation:
```
1   2   3   4   ... n
n+1 n+2 n+3 n+4 ... 2n
... ... ... ... ... ...
... ... ... ... ... ...
n(n-1)+1 .. ... ... n^2
```
Where each number represents a spot on the chess board. Each spot can be represented with a 0 or 1, which means a queen is not there or there respectively. The goal condition is to have y number of 1's on the board that are all neither in the same row, column, or diagonal from one another.

- Goal/Termination Condition: All queens are placed on the board and cannot be killed by another queen.

### C. Intelligent Agents

#### i. Intelligent Thermostat

- Performance Measure: Internal temperatures, Reduced heating/cooling bills

- Environment: Households, Businesses, Areas with varying temperatures

- Actuators: Air vents, Boiler, Display of information, Phone applications

- Sensors: Thermometer, Clock, Touch Screen, Rotating Dial (to manually set temperature)

#### ii. Intelligent Television Console

- Performance Measure: Color, Brightness, Accuracy of voice commands, Accuracy of profile choice, Speed of detection

- Environment Households: Households with 2+ people, People with different TV preferences

- Actuators: Television screen, Remote control lights, Television volume

- Sensors: Remote control inputs, Microphones (voice commands), Light sensors (to dim or brighten screen according to environment), Cameras (facial recognition for profile choice)

[source]: https://www.nytimes.com/2019/03/14/technology/facebook-whatsapp-outage.html
