<h1>Carpe Diem Shipping</h1>
<p>Carpe Diem Shipping takes the weight of a package and determines the cheapest way to ship that package.</p>
<p> The customer has 3 options in this flow control project:-
<br>
<h4>GROUND SHIPPING</h4>
<p>Has a small flat charge ($20) plus a rate based on the weight of the package.</p>

<p>Weight of Package</p>
<li>2 lb or less @ $4.50</li>
<li>Over 2 lb but less than or equal to 6 lb @ 9.00</li>
<li>Over 6 lb but less than or equal to 10 lb @ 12.00</li>
<li>Over 10 lb @ 14.25</li>

<br>
<p>Note: A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping</p>

<br>
<h4>GROUND SHIPPING PREMIUM</h4>
<p>Has a flat charge ($125.00), but no charge for weight</p>

<br>
<h4>DRONE SHIPPING</h4>
<p>Has no flat charge, but the rate based on weight is triple the rate of ground shipping.</p>

<p>Weight of Package</p>
<li>2 lb or less@ $4.50</li>
<li>Over 2 lb but less than or equal to 6 lb @ $9.00</li>
<li>Over 6 lb but less than or equal to 10 lb @ $12.00</li>
<li>Over 10 lb @ $14.25</li>

<br>
<p>Note: A package that weighs 1.5 pounds should cost $6.75 to ship by drone</p>

<br>
<p>The output of the program will have the following format:</p>

  <ul><b>Asks: [Weight]</b></ul>
 <br>
  <ul><b>Ground Shipping $ : [Answer]</b></ul>
  <ul><b>Ground Shipping Premimium $: [Answer]</b></ul>
  <ul><b>Drone Shipping: $: [Answer]</b></ul>

<br>
<p>Example 1:</p>
<p><b>For 4.8 pounds, ground shipping is the cheapest:</b></p>
  <ul><b>Weight:  4.8</b></ul>

  <ul>Ground Shipping $ 34.4</ul>
  <ul>Ground Shipping Premimium $ 125.0</ul>
  <ul>Drone Shipping: $ 43.199999999999996</ul>

<p>Example 2:</p>
<p><b>For 41.5 pounds, ground shipping premium is the cheapest:</b></p>
  <ul><b>Weight:  41.5</b></ul>

  <ul>Ground Shipping $ 217.125</ul>
  <ul>Ground Shipping Premimium $ 125.0</ul>
  <ul>Drone Shipping: $ 591.375</ul>
