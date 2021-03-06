# Xiaomi Yi Action Camera
| | |
|-------------|-----------|
| Model       | YDXJ-v22  |
| Firmware    | 1.2.13    |
| HW Revision | 22 (Z221) |

## Specs

### Camera
| | |
|-------------------------|------------------------------------------|
| Sensor                  | Sony Exmor R BSI CMOS                    |
| Processor               | [Ambarella A7LS](http://www.ambarella.com/uploads/docs/A7LS-Brief-121713.pdf) |
| Max Aperture            | F2.8                                     |
| Field of View (Degrees) | 155                                      |
| Focus                   | Locked (Manual adjustment inside camera) |

### CPU
| | |
|------------------|-----------------------------------------|
| Processor        | ARMv6-compatible processor rev 5 (v6l)  |
| BogoMIPS         | 517.73                                  |
| Features         | swp half thumb fastmult edsp java       |
| CPU implementer  | 0x41                                    |
| CPU architecture | 6TEJ                                    |
| CPU variant      | 0x1                                     |
| CPU part         | 0xb36                                   |
| CPU revision     | 5                                       |
| Hardware         | A7L_BUB_Boss                            |
| Revision         | 1d4c1041                                |

### Memory
| | |
|----------|------|
| Total    | 36MB |
| Used     | 21MB |

### Disk
| | |
|-----------|---------|
| Read Seq  | 6.7MB/s |
| Write Seq | 6.0MB/s |

### Network
| | |
|---------------|------|
| 

## Features
| Features      | Supported |
|---------------|-----------|
| USB Storage   | Yes       |
| Webcam        | No        |
| Linux Console | Yes       |
| Wifi          | Yes       |

## Getting console access
Default WIFI Password is 1234567890.

Create the file 'enable_info_display.script', in the root of the SDCard. Reboot camera, then telnet to camera IP.
Login: root
Password: -none-

## Special files
| | |
|---|---|
| enable_info_display.script | Enable telnet login |
| autoexec.ash | Camera settings set on boot |
