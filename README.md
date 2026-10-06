# Adrienn Varn - Cash Register Lab

Cash Register lab for Flatiron School, SE-FND2-FT Module 3.

The structure of this project is terrible. This isn't how to implement these things at _all_. 
- Items list is completely redundant.
- Total should be dynamically recalculated from prices and quantities in transaction list.
- Applying discount to total isn't implemented correctly in project requirements. If you add an item, call apply_discount, and then add another item and call it again, the first item would be discounted twice. Removing the last transaction item on discount is completely pointless.
- Voiding transaction doesn't recalculate discount on total (not that it matters, given that the discount calculation is completely wrong).
