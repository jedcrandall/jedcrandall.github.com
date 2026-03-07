#/bin/bash

# <p><a href="http://people.csail.mit.edu/moein/papers/sparsdr-mobisys19.pdf">http://people.csail.mit.edu/moein/papers/sparsdr-mobisys19.pdf</a></p>

echo "Enter the URL:" >&2
read url
echo "Enter the title:" >&2
read title
echo -n "<p><a href = \""
echo -n $url
echo -n "\">"
echo -n $title
echo "</a></p>"
