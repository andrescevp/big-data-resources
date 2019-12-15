#SYSTEM INFORMATION
- Display Linux system information: 
```bash
uname -a
```

- Display kernel release information: 
```bash
uname -r
```

- Show which version of redhat installed: 
```bash
cat /etc/redhat-release
```

- Show how long the system has been running + load: 
```bash
uptime
```

- Show system host name: 
```bash
hostname
```

- Display the IP addresses of the host: 
```bash
hostname -I
```

- Show system reboot history: 
```bash
last reboot
```

- Show the current date and time: 
```bash
date
```

- Show this month's calendar: 
```bash
cal
```

- Display who is online: 
```bash
w
```

- Who you are logged in as: 
```bash
whoami
```
#HARDWARE INFORMATION
- Display messages in kernel ring buffer: 
```bash
dmesg
```

- Display CPU information: 
```bash
cat /proc/cpuinfo
```

- Display memory information: 
```bash
cat /proc/meminfo
```

- Display free and used memory ( -h for human readable, -m for MB, -g for GB.): 
```bash
free -h
```

- Display PCI devices: 
```bash
lspci -tv
```

- Display USB devices: 
```bash
lsusb -tv
```

- Display DMI/SMBIOS (hardware info) from the BIOS: 
```bash
dmidecode
```

- Show info about disk sda: 
```bash
hdparm -i /dev/sda
```

- Perform a read speed test on disk sda: 
```bash
hdparm -tT /dev/sda
```

- Test for unreadable blocks on disk sda: 
```bash
badblocks -s /dev/sda
```
#PERFORMANCE MONITORING AND STATISTICS
- Display and manage the top processes: 
```bash
top
```

- Interactive process viewer (top alternative): 
```bash
htop
```

- Display processor related statistics: 
```bash
mpstat 1
```

- Display virtual memory statistics: 
```bash
vmstat 1
```

- Display I/O statistics: 
```bash
iostat 1
```

- Display the last 100 syslog messages  (Use /var/log/syslog for Debian based systems.): 
```bash
tail 100 /var/log/messages
```

- Capture and display all packets on interface eth0: 
```bash
tcpdump -i eth0
```

- Monitor all traffic on port 80 ( HTTP ): 
```bash
tcpdump -i eth0 'port 80'
```

- List all open files on the system: 
```bash
lsof
```

- List files opened by user: 
```bash
lsof -u user
```

- Display free and used memory ( -h for human readable, -m for MB, -g for GB.): 
```bash
free -h
```

- Execute "df -h", showing periodic updates: 
```bash
watch df -h
```
#USER INFORMATION AND MANAGEMENT
- Display the user and group ids of your current user.: 
```bash
id
```

- Display the last users who have logged onto the system.: 
```bash
last
```

- Show who is logged into the system.: 
```bash
who
```

- Show who is logged in and what they are doing.: 
```bash
w
```

- Create a group named "test".: 
```bash
groupadd test
```

- Create an account named john, with a comment of "John Smith" and create the user's home directory.: 
```bash
useradd -c "John Smith" -m john
```

- Delete the john account.: 
```bash
userdel john
```

- Add the john account to the sales group: 
```bash
usermod -aG sales john
```
#FILE AND DIRECTORY COMMANDS
- List all files in a long listing (detailed) format: 
```bash
ls -al
```

- Display the present working directory: 
```bash
pwd
```

- Create a directory: 
```bash
mkdir directory
```

- Remove (delete) file: 
```bash
rm file
```

- Remove the directory and its contents recursively: 
```bash
rm -r directory
```

- Force removal of file without prompting for confirmation: 
```bash
rm -f file
```

- Forcefully remove directory recursively: 
```bash
rm -rf directory
```

- Copy file1 to file2: 
```bash
cp file1 file2
```

- Copy source_directory recursively to destination. If destination exists, copy source_directory into destination, otherwise create destination with the contents of source_directory.: 
```bash
cp -r source_directory destination
```

- Rename or move file1 to file2. If file2 is an existing directory, move file1 into directory file2: 
```bash
mv file1 file2
```

- Create symbolic link to linkname: 
```bash
ln -s /path/to/file linkname
```

- Create an empty file or update the access and modification times of file.: 
```bash
touch file
```

- View the contents of file: 
```bash
cat file
```

- Browse through a text file: 
```bash
less file
```

- Display the first 10 lines of file: 
```bash
head file
```

- Display the last 10 lines of file: 
```bash
tail file
```

- Display the last 10 lines of file and "follow" the file as it grows.: 
```bash
tail -f file
```
#PROCESS MANAGEMENT
- Display your currently running processes: 
```bash
ps
```

- Display all the currently running processes on the system.: 
```bash
ps -ef
```

- Display process information for processname: 
```bash
ps -ef | grep processname
```

- Display and manage the top processes: 
```bash
top
```

- Interactive process viewer (top alternative): 
```bash
htop
```

- Kill process with process ID of pid: 
```bash
kill pid
```

- Kill all processes named processname: 
```bash
killall processname
```

- Start program in the background: 
```bash
program &
```

- Display stopped or background jobs: 
```bash
bg
```

- Brings the most recent background job to foreground: 
```bash
fg
```

- Brings job n to the foreground: 
```bash
fg n
```
#FILE PERMISSIONS

![file schema](img/linux-permissions-chart.png)

```bash

#Linux chmod example
        PERMISSION      EXAMPLE

         U   G   W
        rwx rwx rwx     chmod 777 filename
        rwx rwx r-x     chmod 775 filename
        rwx r-x r-x     chmod 755 filename
        rw- rw- r--     chmod 664 filename
        rw- r-- r--     chmod 644 filename

# NOTE: Use 777 sparingly!: 

        LEGEND
        U = User
        G = Group
        W = World

        r = Read
        w = write
        x = execute
        - = no access: 
```
#NETWORKING

- Display all network interfaces and ip address: 
```bash
ifconfig -a
```

- Display eth0 address and details: 
```bash
ifconfig eth0
```

- Query or control network driver and hardware settings: 
```bash
ethtool eth0
```

- Send ICMP echo request to host: 
```bash
ping host
```

- Display whois information for domain: 
```bash
whois domain
```

- Display DNS information for domain: 
```bash
dig domain
```

- Reverse lookup of IP_ADDRESS: 
```bash
dig -x IP_ADDRESS
```

- Display DNS ip address for domain: 
```bash
host domain
```

- Display the network address of the host name.: 
```bash
hostname -i
```

- Display all local ip addresses: 
```bash
hostname -I
```

- Download http://domain.com/file: 
```bash
wget http://domain.com/file
```

- Display listening tcp and udp ports and corresponding programs: 
```bash
netstat -nutlp
```
 

#ARCHIVES (TAR FILES)
- Create tar named archive.tar containing directory.: 
```bash
tar cf archive.tar directory
```

- Extract the contents from archive.tar.: 
```bash
tar xf archive.tar
```

- Create a gzip compressed tar file name archive.tar.gz.: 
```bash
tar czf archive.tar.gz directory
```

- Extract a gzip compressed tar file.: 
```bash
tar xzf archive.tar.gz
```

- Create a tar file with bzip2 compression: 
```bash
tar cjf archive.tar.bz2 directory
```

- Extract a bzip2 compressed tar file.: 
```bash
tar xjf archive.tar.bz2
```
#INSTALLING PACKAGES
- Search for a package by keyword.: 
```bash
yum search keyword
```

- Install package.: 
```bash
yum|apt|apt-get install package
```

- Display description and summary information about package.: 
```bash
yum info package
```

- Install package from local file named package.rpm: 
```bash
rpm -i package.rpm
```

- Remove/uninstall package.: 
```bash
yum remove package
```

- Install software from source code.: 
```bash
tar zxvf sourcecode.tar.gz
cd sourcecode
./configure
make
make install
```
#SEARCH
- Search for pattern in file: 
```bash
grep pattern file
```

- Search recursively for pattern in directory: 
```bash
grep -r pattern directory
```

- Find files and directories by name: 
```bash
locate name
```

- Find files in /home/john that start with "prefix".: 
```bash
find /home/john -name 'prefix*'
```

- Find files larger than 100MB in /home: 
```bash
find /home -size +100M
```
#SSH LOGINS
- Connect to host as your local username.: 
```bash
ssh host
```

- Connect to host as user: 
```bash
ssh user@host
```

- Connect to host using port: 
```bash
ssh -p port user@host
```
#FILE TRANSFERS
- Secure copy file.txt to the /tmp folder on server: 
```bash
scp file.txt server:/tmp
```

- Copy *.html files from server to the local /tmp folder.: 
```bash
scp server:/var/www/*.html /tmp
```

- Copy all files and directories recursively from server to the current system's /tmp folder.: 
```bash
scp -r server:/var/www /tmp
```

- Synchronize /home to /backups/home: 
```bash
rsync -a /home /backups/
```

- Synchronize files/directories between the local and remote system with compression enabled: 
```bash
rsync -avz /home server:/backups/
```
#DISK USAGE
- Show free and used space on mounted filesystems: 
```bash
df -h
```

- Show free and used inodes on mounted filesystems: 
```bash
df -i
```

- Display disks partitions sizes and types: 
```bash
fdisk -l
```

- Display disk usage for all files and directories in human readable format: 
```bash
du -ah
```

- Display total disk usage off the current directory: 
```bash
du -sh
```
#DIRECTORY NAVIGATION
- To go up one level of the directory tree.  (Change into the parent directory.): 
```bash
cd ..
```

- Go to the $HOME directory: 
```bash
cd $HOME
```

- Change to the /etc directory: cd /etc