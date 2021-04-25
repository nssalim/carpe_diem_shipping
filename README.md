<h1>Carpe Diem Shipping</h1>
<p>Carpe Diem Shipping takes the weight of a package and determines the cheapest way to ship that package.</p>
<p> The customer has 3 options in this flow control project:-
<br>
<h4>A - GROUND SHIPPING</h4>
<p>Has a small flat charge ($20) plus a rate based on the weight of the package.</p>

<p>Weight of Package</p>
<li>2 lb or less @ $4.50</li>
<li>Over 2 lb but less than or equal to 6 lb @ 9.00</li>
<li>Over 6 lb but less than or equal to 10 lb @ 12.00</li>
<li>Over 10 lb @ 14.25</li>

<br>
<p><i>Note: A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping</i></p>


<h4>B - GROUND SHIPPING PREMIUM</h4>
<p>Has a flat charge ($125.00), but no charge for weight</p>


<h4>C - DRONE SHIPPING</h4>
<p>Has no flat charge, but the rate based on weight is triple the rate of ground shipping.</p>

<p>Weight of Package</p>
<li>2 lb or less@ $4.50</li>
<li>Over 2 lb but less than or equal to 6 lb @ $9.00</li>
<li>Over 6 lb but less than or equal to 10 lb @ $12.00</li>
<li>Over 10 lb @ $14.25</li>

<br>
<p><i>Note: A package that weighs 1.5 pounds should cost $6.75 to ship by drone<i></p>

<br>
<br>
<p><b>The output of the program will have the following format:</b></p>

  <ul><b>Asks: [Weight]</b></ul>
  
  <ul>Ground Shipping $ : [Answer]</ul>
  <ul>Ground Shipping Premimium $: [Answer]</ul>
  <ul>Drone Shipping: $: [Answer]</ul>

<br>
<p>Example 1:</p>
<p><b>For 4.8 pounds, GROUND SHIPPING is the cheapest:</b></p>
  <ul>Weight:  4.8</ul>

  <ul><b>Ground Shipping $ 34.4</b></ul>
  <ul>Ground Shipping Premium $ 125.0</ul>
  <ul>Drone Shipping: $ 43.199999999999996</ul>

<p>Example 2:</p>
<p><b>For 41.5 pounds, GROUND SHIPPING PREMIUM is the cheapest:</b></p>
  <ul>Weight:  41.5</ul>

  <ul>Ground Shipping $ 217.125</ul>
  <ul><b>Ground Shipping Premium $ 125.0</b></ul>
  <ul>Drone Shipping: $ 591.375</ul>
