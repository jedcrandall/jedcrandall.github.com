# Homework 3 hints

In [this screenshot](Screenshot from 2022-11-22 09-31-19.png) you'll see a lot
of DNS traffic that is local.  You should ignore all of it, it's not related to
the attack or assignment.

In [this screenshot](Screenshot from 2022-11-22 09-31-38.png) you'll see a filter you can apply to easily ignore all the local DNS stuff.

In [this screenshot](Screenshot from 2022-11-22 09-32-11.png) you'll see what you get if you click on packet 481 in the attacker pcap and say "Follow" and "UDP Stream".  This is what a normal VPN conection looks like.  The client connects to the server and nothing is funny or out of the ordinary about this flow where teh attacker successfully connects to the VPN server.

In [this screenshot](Screenshot from 2022-11-22 09-35-15.png) note the frame numbers, which pcap it's in, and the IPID.

In [this screenshot](Screenshot from 2022-11-22 09-36-47.png) note the same.  Then check out Figure 18 in [this blog post](https://breakpointingbad.com/2021/09/08/Port-Shadows-via-Network-Alchemy.html).  Step 3.1 is where this packet is generated, and you're seeing it in both packet captures.  The blog post is not easy to follow, but we'll go over it in class on 11/22 and can go over it again in future classes.  When two VPN clients send connection requests to the same VPN server, the server should recieve both of those requests.  For one client to recieve the other client's request is definitely not something you'll see with proper security and privacy that is in line with what VPN users expect.
