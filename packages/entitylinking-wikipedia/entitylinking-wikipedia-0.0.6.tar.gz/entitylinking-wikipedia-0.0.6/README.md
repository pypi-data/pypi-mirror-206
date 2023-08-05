<h3>Entity Linking via WikiPedia </h3>

This package is used to perform Entity Linking based on Wikipedia based on user's input sentence.

Check out below github page for more details:
https://github.com/pypa/sampleproject

<h3>Installation of Package</h3>

pip install entitylinking-wikipedia


<h3>Sample Coding using this Package</h3>

from  import * <br>
import pandas as pd <br>
final_out = pd.DataFrame() <br>
final_out = Entity_Linking_via_Wikipedia('I stay in Kolkata in India.') <br>
print(final_out) <br>