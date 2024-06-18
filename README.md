# pyWordManager
a simple password manager written in python.

pyWordManager is a locally run password manager via the terminal. Design decisions were made utilising [OWASP](https://owasp.org/) recommended implementations.

## Design Decisions

### Master Password Authentication
Authentication is done using Galois/Counter Mode (GCM) tag when decrypting the file itself.
If decryption fails the exception handler catches it and returns null, indicating that
authentication has failed.

The choice of having an authentication system that does not check hash as it would
traditionally. this method was chosen as it would then required to store it and is similar to
how other local password managers do authentication [1](https://support.1password.com/authentication-encryption/)

The key for decryption is then the hash of the master password which is created using a key
deriving function. PBKDF2 was the initial choice but was then replaced by Argon2 with a
hash length of 256bit.

GCM mode was selected as OWASP states ”should be used as a first preference”

### Pseudo-Random Number Generator
For generating passwords the secret Modules choice function was used. To select a
character from the provided options
```
for x in range(length):
password += secrets.choice(
string.ascii_letters +
string.digits +
string.punctuation
)
return password
```
The secret module implements the os modules’ random number functions. Which is stated to
be cryptographically secure [3](https://cryptography.io/en/latest/random-numbers/). And is recommended in the
OWASP cheat sheet [3](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html).urandom was used to get iv and salts.
```
iv = os.urandom(16)
```


# Design
## Context Level

<img align="left" class="context level design" src="./readme.assets/f.png" style="width:180px">

<br clear="left"/>


## Container Level
<img src="./readme.assets/sdfa.png" alt="container level design" style="width:450px"/>

## Component Level
<img align="right" src="./readme.assets/sadsaf.png" alt="component level: create user" style="width:450px"/>

### Create User Component

<br clear="right"/>

<img align="right" src="./readme.assets/savepasswordcontainer.png" alt="component level: save password" style="width:450px"/>

### Save Password Component

<br clear="right"/>

<img align="right" src="./readme.assets/unnamed.png" alt="component level: get password" style="width:450px"/>

### Get Password Component
