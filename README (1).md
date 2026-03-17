# 🔐 Geffe Generator Keystream (LFSR-Based)

```{=html}
<p align="center">
```
`<b>`{=html}Stream Cipher \| Cryptography \| LFSR \| Geffe
Generator`</b>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 📌 Overview

This project demonstrates a **Geffe Generator**, a keystream generator
used in stream ciphers.\
It combines multiple **Linear Feedback Shift Registers (LFSRs)** to
produce a **non-linear and secure pseudo-random sequence**.

------------------------------------------------------------------------

## 🎯 Project Highlights

-   🔁 3 × 4-bit LFSRs
-   🧮 Primitive polynomials
-   ⚡ Non-linear Geffe combining function
-   🔐 Improved randomness vs single LFSR
-   🖥️ Beginner-friendly Python implementation

------------------------------------------------------------------------

## 🏗️ System Architecture

                     ┌────────────────────┐
                     │   12-bit KEY Input │
                     └─────────┬──────────┘
                               │
                   ┌───────────┬──────┴──────┬
                   │           │             │           
                   k1          k2            k3
                   │           │             │
               ┌────────┐  ┌────────┐  ┌────────┐
               │ LFSR 1 │  │ LFSR 2 │  │ LFSR 3 │
               └────────┘  └────────┘  └────────┘
                   │           │             │
                   x1          x2            x3
                   └──────┬────┴──────┬─────┘
                          │           │
                    ┌──────────────────────┐
                    │   Geffe Generator    │
                    └─────────┬────────────┘
                              │
                          Final KEY

------------------------------------------------------------------------

## 🔄 Workflow

### Step 1: Input

Enter 12-bit binary key:

    101100111010

### Step 2: Split Key

    k1 = first 4 bits
    k2 = next 4 bits
    k3 = last 4 bits

### Step 3: LFSR Processing

  LFSR    Polynomial             Feedback
  ------- ---------------------- ---------------------------
  LFSR1   x⁴ + x + 1             bit4 ⊕ bit1
  LFSR2   x⁴ + x³ + 1            bit4 ⊕ bit3
  LFSR3   x⁴ + x³ + x² + x + 1   bit4 ⊕ bit3 ⊕ bit2 ⊕ bit1

Each runs for **15 cycles**.

------------------------------------------------------------------------

## 🔗 Geffe Combining Function

    KEY = (x1 & x2) ^ (x2 & x3) ^ (x3)

------------------------------------------------------------------------

## 📊 Data Flow Diagram

    k1 ──► LFSR1 ──► x1 ─┐
                         │
    k2 ──► LFSR2 ──► x2 ─┼──► Geffe Function ─► KEY
                         │
    k3 ──► LFSR3 ──► x3 ─┘

------------------------------------------------------------------------

## 📸 Sample Output

    Enter key: 101100111010

    LFSR1 Output: [...]
    x1 = 11407

    LFSR2 Output: [...]
    x2 = 11702

    LFSR3 Output: [...]
    x3 = 10570

    Final KEY = XXXXX

------------------------------------------------------------------------


## 🧩 Project Structure

    📁 Project
     ├── LFSR.py
     └── README.md

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   🌐 Web UI using Flask
-   📊 Visualization of bit shifting
-   🔄 Support for n-bit LFSRs
-   📁 Export keystream to file

------------------------------------------------------------------------

## 🏆 Ideal For

-   Cryptography learning
-   Mini projects
-   Academic submissions
-   LinkedIn portfolio showcase

------------------------------------------------------------------------

## 👨‍💻 Author

**Hemanth Gowda A**

------------------------------------------------------------------------

⭐ If you like this project, consider giving it a star on GitHub!
