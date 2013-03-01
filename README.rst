====================
Index Helper Scripts
====================

generate-links.py
  This program takes two arguments: the page to link to, and the kind of thing
  being linked.  It then takes as standard input a list of topics, one on each
  line.  The output is a list of generated links.

generate-uniform-links.py
  This program takes two arguments: the base name of the page to link to, and 
  the kind of thing being linked.  It then takes as standard input a list of 
  topics, one on each line.  The output is a list of generated links.
  
  That is to say, running this program with arguments X and Y, input Z on each
  line will result in an output line [[X-z|Z (Y)]], where z is Z changed to
  lowercase and with spaces changed to hyphens.

extract-links.py
  This script takes as input the text of a page and prints as output all of the 
  links in the page.

extract-talents.py
  This script takes advantage of the fact that most of the talent pages have 
  the name of the talent at the beginning of the line (more precisely just 
  after the bullet, but the bullet is dropped when copying and pasting the raw 
  text) followed by a semicolon.  Run it with the name of the page to be linked 
  as the first argument and copy and paste the page into the program after you 
  run it (followed by typing Control-D once or twice).  Note that occasionally 
  there will be other words with this format so you need to scan the resulting 
  list for mistakes before using it.

update-index.py
  The following script takes as input the source code for the old version of 
  the index followed by a list of links and its sorts all of the index links, 
  automatically creating or deleting letter sections. The link extractor 
  automatically puts the links in the correct format for input to this program, 
  so the idea is that you take a page, extract all of its links, do some extra 
  formatting of these links (such as adding "(class)" to classes), removing 
  links that should appear in the index (such as those to the the main page), 
  and then construct the new index by running the following script, copying and 
  pasting the old index source code, copying and pasting the new links that you 
  just formatted, pressing Control-D once or twice to let the script know you 
