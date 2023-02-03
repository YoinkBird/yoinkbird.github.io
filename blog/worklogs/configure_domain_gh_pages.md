# Worklog - 2023-02-01: Configure Domain for Github Pages

Part 3/3 of [Overhaul of the Github Pages Website](./overhaul_gh_pages.md)

**Goal**: "Point" yoinkbird.com to [yoinkbird.github.io](https://yoinkbird.github.io)

## Update DNS

### Subdomain

Initial approach: Just update CNAME and then verify ownership, as per https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain

```bash
$ dig www.yoinkbird.com +nostats +nocomments +nocmd
;www.yoinkbird.com.		IN	A
www.yoinkbird.com.	355	IN	CNAME	yoinkbird.github.io.
yoinkbird.github.io.	355	IN	A	185.199.108.153
yoinkbird.github.io.	355	IN	A	185.199.109.153
yoinkbird.github.io.	355	IN	A	185.199.111.153
yoinkbird.github.io.	355	IN	A	185.199.110.153
github.io.		355	IN	NS	dns4.p05.nsone.net.
github.io.		355	IN	NS	dns3.p05.nsone.net.
github.io.		355	IN	NS	dns2.p05.nsone.net.
github.io.		355	IN	NS	ns-1622.awsdns-10.co.uk.
github.io.		355	IN	NS	ns-393.awsdns-49.com.
github.io.		355	IN	NS	dns1.p05.nsone.net.
github.io.		355	IN	NS	ns-1339.awsdns-39.org.
github.io.		355	IN	NS	ns-692.awsdns-22.net.
dns2.p05.nsone.net.	355	IN	A	198.51.45.5
dns3.p05.nsone.net.	355	IN	A	198.51.44.69
dns2.p05.nsone.net.	355	IN	AAAA	2a00:edc0:6259:7:5::2
ns-1622.awsdns-10.co.uk. 355	IN	A	205.251.198.86
ns-1339.awsdns-39.org.	355	IN	A	205.251.197.59
ns-393.awsdns-49.com.	355	IN	A	205.251.193.137
dns3.p05.nsone.net.	355	IN	AAAA	2620:4d:4000:6259:7:5:0:3
ns-1622.awsdns-10.co.uk. 355	IN	AAAA	2600:9000:5306:5600::1
ns-692.awsdns-22.net.	355	IN	A	205.251.194.180
dns1.p05.nsone.net.	355	IN	A	198.51.44.5
dns1.p05.nsone.net.	355	IN	AAAA	2620:4d:4000:6259:7:5:0:1
ns-393.awsdns-49.com.	355	IN	AAAA	2600:9000:5301:8900::1
dns4.p05.nsone.net.	355	IN	A	198.51.45.69
ns-692.awsdns-22.net.	355	IN	AAAA	2600:9000:5302:b400::1
ns-1339.awsdns-39.org.	355	IN	AAAA	2600:9000:5305:3b00::1
dns4.p05.nsone.net.	355	IN	AAAA	2a00:edc0:6259:7:5::4
```

Then update GH:
https://github.com/YoinkBird/yoinkbird.github.io/settings/pages

#### Issue

This simple "Configuring a subdomain" step will, as it says on the tin, not configure the apex domain.

I.e. visits directly to `yoinkbird.com` will not be redirected to the yoinkbird.github.io page.

This is, however, desirable, so it becomes necessary to configure the registrar's A-records accordingly.

### Configuring an apex domain

Allow `yoinkbird.com` to go directly to `yoinkbird.github.io` as well (in addtion to `www.yoinkbird.com`).

Instructions: Both https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain and https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain-and-the-www-subdomain-variant

Caveat: The github pages docs mention a ["github pages DNS records"](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain); this is _most likely_ a roundabout way of referring to DNS records created based on the `CNAME` file present in the repo, and not an actual user-facing DNS record interface.

Caveat: building directly off of the "Configuring a subdomain" step, i.e. leaving GH Pages config with the `www` subdomain, in order to manage the apex domain entirely via the registrar.

Verify:


**Verify DNS for apex domain**:

```
$ dig yoinkbird.com +nocmd +nostats
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 36603
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 2, ADDITIONAL: 3

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;yoinkbird.com.			IN	A

;; ANSWER SECTION:
yoinkbird.com.		872	IN	A	185.199.111.153
yoinkbird.com.		872	IN	A	185.199.109.153
yoinkbird.com.		872	IN	A	185.199.108.153
yoinkbird.com.		872	IN	A	185.199.110.153

;; AUTHORITY SECTION:
yoinkbird.com.		872	IN	NS	ns2.hover.com.
yoinkbird.com.		872	IN	NS	ns1.hover.com.

;; ADDITIONAL SECTION:
ns2.hover.com.		872	IN	A	64.98.148.13
ns1.hover.com.		872	IN	A	216.40.47.26
```

Observations:

* A-records (Answer section) pointing to GH Pages IPs (as configured via registrar)
* Name-server (Authority) via registrar


**Verify DNS for sub-domain**:
```
$ dig www.yoinkbird.com +nocmd +nostats
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 49542
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 5, ADDITIONAL: 9

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;www.yoinkbird.com.		IN	A

;; ANSWER SECTION:
www.yoinkbird.com.	782	IN	CNAME	yoinkbird.github.io.
yoinkbird.github.io.	782	IN	A	185.199.110.153
yoinkbird.github.io.	782	IN	A	185.199.108.153
yoinkbird.github.io.	782	IN	A	185.199.111.153
yoinkbird.github.io.	782	IN	A	185.199.109.153

;; AUTHORITY SECTION:
github.io.		782	IN	NS	dns2.p05.nsone.net.
github.io.		782	IN	NS	ns-692.awsdns-22.net.
github.io.		782	IN	NS	dns1.p05.nsone.net.
github.io.		782	IN	NS	ns-1622.awsdns-10.co.uk.
github.io.		782	IN	NS	dns3.p05.nsone.net.

;; ADDITIONAL SECTION:
dns2.p05.nsone.net.	782	IN	AAAA	2a00:edc0:6259:7:5::2
dns1.p05.nsone.net.	782	IN	AAAA	2620:4d:4000:6259:7:5:0:1
dns3.p05.nsone.net.	782	IN	A	198.51.44.69
dns1.p05.nsone.net.	782	IN	A	198.51.44.5
dns3.p05.nsone.net.	782	IN	AAAA	2620:4d:4000:6259:7:5:0:3
dns2.p05.nsone.net.	782	IN	A	198.51.45.5
ns-692.awsdns-22.net.	782	IN	A	205.251.194.180
ns-1622.awsdns-10.co.uk. 782	IN	A	205.251.198.86

```

Observations:

* A-records (Answer section) pointing to GH Pages IPs (as configured via GH)
* Authority (Authority) via github

**Certificate**:
```
$ echo | openssl s_client -showcerts -servername yoinkbird.com -connect yoinkbird.com:443 2>/dev/null | openssl x509 -inform pem -noout -text | grep -A 1 'Subject Alternative Name'
            X509v3 Subject Alternative Name: 
                DNS:www.yoinkbird.com, DNS:yoinkbird.com

```

A-record (for apex domain):
```
$ dig yoinkbird.com +noall +answer -t A
yoinkbird.com.		628	IN	A	185.199.108.153
yoinkbird.com.		628	IN	A	185.199.110.153
yoinkbird.com.		628	IN	A	185.199.109.153
yoinkbird.com.		628	IN	A	185.199.111.153

```

### Verify Domain

Following [https://github.com/settings/pages_verified_domains/new](https://github.com/settings/pages_verified_domains/new) via <https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages>



Add TXT record at registrar

Then click [verify]:

```
Successfully verified yoinkbird.com 

```

```bash
$ dig _github-pages-challenge-YoinkBird.yoinkbird.com +nostats +nocomments +nocmd TXT
;_github-pages-challenge-YoinkBird.yoinkbird.com. IN TXT
_github-pages-challenge-YoinkBird.yoinkbird.com. 886 IN	TXT "<CHALLENGE>"
```



# Conclusion


All goals met, although the GH pages for domains get a bit confusing and there's a lot of "automagic" they don't document.

Best to plan in about a day to let all DNS changes propagate, and remember to always check both the generated certificate and the DNS records when troubleshooting!

