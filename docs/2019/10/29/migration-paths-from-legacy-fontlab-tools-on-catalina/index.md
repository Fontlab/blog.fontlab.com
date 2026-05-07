If you rely on FontLab Studio 5, Fontographer 5, TypeTool 3, or BitFonter 3 on a Mac that has been updated to macOS Catalina, there are three viable routes: CrossOver Mac 19 for a lightweight Windows emulation layer, a virtual machine running an older macOS or Windows, or a clean upgrade to FontLab 7. This post covers the setup in detail for each option.

## CrossOver Mac 19

[Codeweavers CrossOver Mac](https://www.codeweavers.com/) 19 runs on macOS Catalina and lets you run 32-bit Windows apps without installing Windows — a thin emulation layer that requires no full Windows license.

The whole footprint is small: CrossOver, the Windows bottle, and the FontLab apps together take under 1 GB of disk. CrossOver uses far less RAM than a real Windows virtual machine, and apps run at native speed.

The trade-off: Windows apps on CrossOver still look and behave like Windows apps, not Mac apps.

We've tested FontLab Studio 5, Fontographer 5, TypeTool 3, and BitFonter 3 with CrossOver 19 — they run fine. [Contact our sales](https://www.fontlab.com/contact/) for cross-grade pricing from Mac to Windows versions of the classic apps.

## Virtualization

### Running macOS inside macOS

Virtualization apps let you run a complete operating system inside a window on your Mac. The guest OS lives on a virtual disk — a large file on your real drive — and runs alongside your normal apps. From the guest's perspective, the virtual machine is the computer.

You can configure shared folders so the guest can read and write files on your real Mac, just like a network drive. Some virtualization apps also offer a "coherence" mode where guest app windows appear alongside real Mac windows.

**Performance:** you assign a fixed slice of RAM to the VM when it runs. Font editors are not memory-hungry — 4 GB is plenty. As for speed, modern Macs support hardware virtualization via a hypervisor. Guest apps typically run at 80–90% of native speed, which is faster than FontLab Studio 5 ran on Macs from just a few years ago. You won't notice any delays.

### Choose your virtualization app

Three options exist for Mac:

**[Parallels Desktop 15](https://www.parallels.com/products/desktop/)** is the most popular. Easy to use, runs Catalina as host, and lets you install macOS Mojave, High Sierra, or Sierra as a guest. Standard edition: $80/€100 one-time, or €80/year subscription with free upgrades. Pro edition costs about $20 more.

**[VMWare Fusion 11.5](https://www.vmware.com/products/fusion.html)** is the alternative. Performance is comparable to Parallels (marginally faster in some tests, marginally slower in others). VMs created in VMWare are slightly more portable — there is a free VMWare Workstation Player for Windows that can run the same VM files. Price: $/€90.

**[Oracle VirtualBox](https://www.virtualbox.org/)** is completely free and open-source. Performance is comparable, but setup is more complex and host/guest integration is less polished. Download the "OS X hosts" version from the VirtualBox website.

### Choose your guest macOS

*The macOS license agreement permits running macOS as a guest only when the host is also macOS. Running macOS inside Windows, or on a PC, is not permitted.*

The easiest choice is **macOS 10.14 Mojave**. A Mojave virtual disk takes around 22 GB once installed; Sierra takes around 11 GB.

Download links (each opens in the Mac App Store or System Preferences):

**macOS 10.14.6 Mojave** — requires at least 2 GB RAM and 18.5 GB storage in the VM. [Download macOS Mojave](https://apps.apple.com/us/app/macos-mojave/id1398502828) (6.1 GB installer)

**macOS 10.13.6 High Sierra** — requires at least 2 GB RAM and 14.3 GB storage in the VM. [Download macOS High Sierra](https://apps.apple.com/us/app/macos-high-sierra/id1246284741) (4.8 GB installer)

**macOS 10.12.6 Sierra** — requires at least 2 GB RAM and 8.8 GB storage in the VM. [Download macOS Sierra](https://itunes.apple.com/us/app/macos-sierra/id1127487414) (5.1 GB installer) — note: you can only download this from the App Store if you are currently on High Sierra or earlier.

### Installing macOS Mojave in Parallels Desktop

Parallels Desktop makes guest macOS installation straightforward. You'll need about 42 GB of free space during installation; once complete, the VM will occupy 23–32 GB.

1. Run *Parallels Desktop*.
1. Choose *File > New…* to open the Installation Assistant.
1. Click *Install Windows or another OS from a DVD or image file* and click *Continue*.
1. In the *Installation images found* list, choose *macOS: Install macOS Mojave.app* and click *Continue*.
1. Click *Continue* in the popup and save the *macOS image file.dmg* in the suggested location (the *Parallels* folder inside your home folder). Wait for the image to be created.
1. In the *Name and Location* window, enter a name. Enable *Create alias on Mac desktop* and *Customize settings before installation*.
1. By default Parallels stores the VM in your *Parallels* folder. If you have both an SSD and an HDD, store it on the SSD.
1. Click *Create*. In the Configuration dialog:
1. *Options* tab → *Optimization > Resource usage*: choose *Medium*
1. *Sharing > Share folders*: you may choose *All disks*
1. *Hardware* tab → *CPU & Memory*: allocate 20–25% of your Mac's RAM (2 GB minimum; 4 GB if you have 16 GB)
1. *Graphics*: set Memory to 256 or 512 MB
1. Click *+ > Hard Disk*, set the maximum virtual disk size (32 GB if you allocated 4 GB RAM), enable *Split the disk image into 2 GB files*, click *OK*
1. Click *Hard Disk 1*, click *–* at the bottom, choose *Move to Trash*
1. In *Boot Order*, click *Hard Disk 2*, then click *↑*
1. Close the Configuration window with the red × button
1. In the Installation Assistant, click *Continue*.
1. Sign in to or create a Parallels Account to start the 14-day trial or activate your purchase.
1. The guest window appears. Click *▶* to start installing macOS Mojave.
1. If Parallels asks to use Accessibility features, click *Grant* and enable it in *System Preferences > Security & Privacy > Accessibility*.
1. When the *Welcome* screen appears in the guest, choose your language and click *→*. Press Ctrl+Alt to release mouse capture back to your real Mac.
1. In the *macOS Utilities* dialog inside the guest, double-click *Install macOS*.
1. Proceed through the installer; choose *Macintosh HD* (the virtual Hard Disk 2, not your real drive).
1. After 10–15 minutes the guest restarts. You don't need to sign in with an Apple ID unless you want to sync data with the guest.
1. Create a user account — same name as your real Mac account is fine, but use a different password.
1. Once setup completes, the guest desktop appears.
1. Click the yellow-triangle exclamation in the guest window's top-right corner and choose *Install Parallels Tools…*
1. Double-click the *Parallels Tools* volume on the guest desktop, double-click install, and complete the installation.
1. Enter the guest account's password when prompted (not your real Mac password).
1. Click *Restart*.
1. After restart, drag the *Parallels Tools* volume to the Bin inside the guest window. From the app menu, choose *Devices > CD/DVD > Disconnect*.
1. Double-click *Parallels Shared Folders* on the guest desktop. The guest Finder will show your real Mac's volumes — you can now open and save files across both systems.
1. On your real Mac, download the latest version of [FontLab Studio 5.1.6](https://www.fontlab.com/font-editor/fontlab-studio/), [Fontographer 5.2.4](https://www.fontlab.com/font-editor/fontographer/), or [TypeTool 3.1.3](https://www.fontlab.com/font-editor/typetool/).
1. Inside the guest, open *Parallels Shared Folders*, navigate to *Home > Downloads*, double-click the DMG, and install the font editor. Enter your serial number to activate.
1. Drag the macOS Mojave VM icon to the left side of your Dock for one-click access.
1. Shut down the guest from its Apple menu.
1. In Parallels Desktop, choose *View > Expanded View*, click the gear icon, go to the *Hardware* tab, click *Hard Disk 1*. If the Source shows *macOS image file.hdd*, click *–* and choose *Move to Trash* — you no longer need the installer volume.
1. Quit Parallels Desktop.
1. Move *Install macOS Mojave.app* from your */Applications* folder to Trash.
1. Empty the Trash — you'll reclaim around 12 GB. Your guest macOS Mojave VM should now occupy no more than 24 GB.

Additional guides for Parallels Desktop:

- <https://www.parallels.com/blogs/try-macos-mojave-parallels-desktop/>
- <https://www.geekrar.com/install-macos-mojave-on-parallels-desktop/>
- <https://www.parallels.com/blogs/older-versions-mac-os-x-with-macos-sierra/>
- <https://www.howtogeek.com/364272/how-to-run-macos-mojave-in-parallels-for-free/>

### Installing guest macOS in VMWare Fusion

- <https://docs.vmware.com/en/VMware-Fusion/11/com.vmware.fusion.using.doc/GUID-474FC78E-4E77-42B7-A1C6-12C2F378C5B9.html>
- <https://www.huibdijkstra.nl/how-to-set-up-a-osx-mojave-vm-in-vmware-fusion/>

### Installing guest macOS in VirtualBox

- <https://www.howtogeek.com/289594/how-to-install-macos-sierra-in-virtualbox-on-windows-10/>
- <https://www.saintlad.com/install-macos-sierra-in-virtualbox-on-windows-10/>
- <https://medium.com/@twister.mr/installing-macos-to-virtualbox-1fcc5cf22801>
- <https://www.maketecheasier.com/install-macos-virtualbox/>

### Tips for managing your guest macOS

Once the guest is running:

- Keep the guest lean — don't install apps you don't need there.
- Save working files on your real Mac using shared folders, not inside the guest.
- In the guest's *System Preferences > General*, switch *Appearance* to *Graphite* so you can tell at a glance whether you're looking at the real desktop or the guest.
- In *Accessibility*, enable *Reduce motion* and *Reduce transparency*.
- Keep the guest in non-Retina mode (the default) — the classic FontLab apps don't support Retina, and non-Retina mode reduces visual confusion.

## Running Windows

### Guest Windows in a virtual machine

Installing a Windows guest works the same way as a macOS guest, and is actually simpler — virtualization apps are most commonly used for Windows. FontLab Studio 5, Fontographer 5, and TypeTool 3 for Windows run on XP, Vista, 7, 8, and 10. [Contact FontLab sales](https://www.fontlab.com/contact/) to cross-grade from a Mac license to a Windows license.

You'll need a valid Windows product key and an ISO installer for your chosen Windows version. An old Windows XP "tiny" or "micro" ISO, once installed, can occupy as little as 2–3 GB. A Windows 7 VM with apps installed typically takes around 9 GB.

### BootCamp with virtualization

Apple's BootCamp lets you install Windows on a separate partition and boot directly into it for full native performance. Parallels Desktop and VMWare Fusion can also run your BootCamp Windows partition inside a VM — slightly slower than native boot, but usable side-by-side with your Mac apps.

## More on this topic

- [FontLab Studio 5, Fontographer 5 and TypeTool 3 on macOS 10.15 Catalina](https://blog.fontlab.com/2019/10/08/fontlab-studio-5-fontographer-5-and-typetool-3-on-macos-1015-catalina/index.md)
