# Comande pyats & genie

```bash
ssh admin@10.202.17.50
setxkbmap fr
cd labs/devnet-src/pyats/
python3 -m venv csr1kv
cd csr1kv/
source bin/activate
pip3 install pyats[full]
pyats run job examples/basic/basic_example_job.py
genie create testbed interactive --output yaml/testbed.yml --encode-password
genie parse "show ip interface brief" --testbed-file yaml/testbed.yml --devices admin123
genie parse "show version" --testbed-file yaml/testbed.yml --devices admin123
genie parse "show ipv6 interface gig 1" --testbed-file yaml/testbed.yml --devices admin123 --output verify-ipv6-1
genie parse "show ipv6 interface gig 1" --testbed-file yaml/testbed.yml --devices admin123 --output verify-ipv6-2
genie diff verify-ipv6-1 verify-ipv6-2
deactivate
```
