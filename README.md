Check domain availability (cli interface)
========

Quickly check domain availability using cli

It uses domainr api and [tabulate](https://pypi.python.org/pypi/tabulate) script to show data.

This is just initial release will update it with more feature soon.

###Few working examples
<pre>
->  python checkdomain.py google.com

    Domain Name    TLD    Availability
    -------------  -----  --------------
    google.com     com    taken
</pre>

<pre>
->  python checkdomain.py google.com cloudtub.com pintext.it cloudtub.net

    Domain Name    TLD    Availability
    -------------  -----  --------------
    google.com     com    taken
    cloudtub.com   com    taken
    pintext.it     it     taken
    cloudtub.net   net    available
</pre>
