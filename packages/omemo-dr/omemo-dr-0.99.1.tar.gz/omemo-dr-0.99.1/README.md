Initial codebase was forked from https://github.com/tgalal/python-axolotl

This is a python port of [libsignal-protocol-java](https://github.com/WhisperSystems/libaxolotl-android) originally written by [Moxie Marlinspike](https://github.com/moxie0)


# Dependencies

 - [protobuf 3.0+](https://github.com/google/protobuf/)
 - [cryptography](https://cryptography.io)

## Linux

```
pip install .
```

# Usage

This python port is done in an almost 1:1 mapping to the original java code. Therefore any original documentation for the java code can be easily mapped and used with this python port.

## Install time

At install time, a libaxolotl client needs to generate its identity keys, registration id, and
prekeys.

```python
    identity_key_pair = KeyHelper.generate_identity_key_pair()
    registration_id   = KeyHelper.generate_registration_id()
    pre_keys          = KeyHelper.generate_pre_keys(start_id, 100)
    last_resort_key   = KeyHelper.generate_last_resort_key()
    signed_pre_key    = KeyHelper.generate_signed_pre_key(identity_key_pair, 5)

    #Store identity_key_pair somewhere durable and safe.
    #Store registration_id somewhere durable and safe.

    #Store pre_keys in PreKeyStore.
    #Store signed prekey in SignedPreKeyStore.
```

## Building a session

A libaxolotl client needs to implement the Store interface. This will manage loading and storing of identity, 
prekeys, signed prekeys, and session state.

Once this is implemented, building a session is fairly straightforward:

```python
store      = MyStore()

# Instantiate a SessionBuilder for a remote recipient_id + device_id tuple.
session_builder = SessionBuilder(store, recipient_id, device_id)

# Build a session with a PreKey retrieved from the server.
sessionBuilder.process(retrieved_pre_key)

session_cipher = SessionCipher(store, recipient_id, device_id)
message        = session_cipher.encrypt("Hello world!")

deliver(message.serialize())
```

# Development

## Generating protobuf files

Download the protobuf-compiler and execute

`protoc -I=omemo_dr/protobuf --python_out=omemo_dr/protobuf OMEMO.proto WhisperTextProtocol.proto LocalStorageProtocol.proto`
