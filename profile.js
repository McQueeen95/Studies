import React from 'react';
import { View, Text, TextInput, StyleSheet, TouchableOpacity } from 'react-native';

const ProfileScreen = () => {
  return (
    <View style={styles.container}>
      <TouchableOpacity style={styles.photoContainer}>
        <Image source={require('./assets/profile-photo.png')} style={styles.photo} />
        <View style={styles.updatePhotoButton}>
          <Text style={styles.updatePhotoButtonText}>Update Photo</Text>
        </View>
      </TouchableOpacity>
      <View style={styles.labelContainer}>
        <Text style={styles.label}>First Name</Text>
        <View style={styles.textInputContainer}>
          <Image source={require('./assets/edit-icon.png')} style={styles.textInputIcon} />
          <TextInput style={styles.textInput} placeholder="Enter your first name" />
        </View>
      </View>
      <View style={styles.labelContainer}>
        <Text style={styles.label}>Last Name</Text>
        <View style={styles.textInputContainer}>
          <Image source={require('./assets/edit-icon.png')} style={styles.textInputIcon} />
          <TextInput style={styles.textInput} placeholder="Enter your last name" />
        </View>
      </View>
      <View style={styles.labelContainer}>
        <Text style={styles.label}>Email</Text>
        <View style={styles.textInputContainer}>
          <Image source={require('./assets/edit-icon.png')} style={styles.textInputIcon} />
          <TextInput style={styles.textInput} placeholder="Enter your email" />
          <TouchableOpacity style={styles.deleteEmailButton}>
            <Image source={require('./assets/delete-icon.png')} style={styles.deleteEmailIcon} />
          </TouchableOpacity>
        </View>
      </View>
      <View style={styles.labelContainer}>
        <Text style={styles.label}>Birthdate</Text>
        <View style={styles.textInputContainer}>
          <Image source={require('./assets/edit-icon.png')} style={styles.textInputIcon} />
          <TextInput style={styles.textInput} placeholder="Enter your birthdate" />
        </View>
      </View>
      <View style={styles.labelContainer}>
        <Text style={styles.label}>Phone Number</Text>
        <View style={styles.textInputContainer}>
          <Image source={require('./assets/edit-icon.png')} style={styles.textInputIcon} />
          <TextInput style={styles.textInput} placeholder="Enter your phone number" />
        </View>
      </View>
      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>Sign Out</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>Reset Password</Text>
      </TouchableOpacity>
    </View>
  );
  
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
    padding: 20,
  },
  profilePhotoContainer: {
    width: 120,
    height: 120,
    borderRadius: 60,
    overflow: 'hidden',
    marginTop: 30,
    marginBottom: 20,
  },
  profilePhoto: {
    flex: 1,
    width: '100%',
    height: '100%',
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    width: '100%',
    marginBottom: 15,
  },
  inputIcon: {
    width: 20,
    height: 20,
    marginRight: 10,
    borderWidth: 1,
    borderColor: '#999',
  },
  input: {
    flex: 1,
    paddingVertical: 10,
    paddingHorizontal: 15,
    backgroundColor: '#eee',
    borderRadius: 5,
    fontSize: 16,
  },
  buttonContainer: {
    width: '100%',
    marginTop: 20,
  },
  button: {
    paddingVertical: 15,
    paddingHorizontal: 30,
    backgroundColor: '#2196F3',
    borderRadius: 5,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
  },
  signOutButton: {
    backgroundColor: '#f44336',
    marginTop: 10,
  },
  deleteEmailButton: {
    backgroundColor: '#f44336',
    marginTop: 10,
  },
  resetPasswordButton: {
    backgroundColor: '#607D8B',
    marginTop: 10,
  },
});

export default ProfileScreen;
