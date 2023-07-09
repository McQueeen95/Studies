import { StatusBar } from "expo-status-bar";
import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  Image,
  TextInput,
  Button,
  TouchableOpacity,
} from "react-native";
export default function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  return (
    <View style={styles.container}>
      <Image style={styles.image} source={require("../../../Users/asus/Downloads/wallpaperflare.com_wallpaper (6).jpg")} /> 
      <StatusBar style="auto" />
      <View style={styles.inputView}>
        <TextInput
          style={styles.TextInput}
          placeholder="Email :"
          placeholderTextColor="#003f5c"
          onChangeText={(email) => setEmail(email)}
        /> 
      </View> 
      <View style={styles.inputView}>
        <TextInput
          style={styles.TextInput}
          placeholder="Password :"
          placeholderTextColor="#003f5c"
          secureTextEntry={true}
          onChangeText={(password) => setPassword(password)}
        /> 
      </View> 
   
      <TouchableOpacity style={styles.loginBtn}>
        <Text style={styles.loginText}>LOGIN</Text> 
      </TouchableOpacity> 
      <TouchableOpacity>
        <Text style={styles.forgot_button}>Forgot Password?</Text> 
      </TouchableOpacity> 
    </View> 
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "black",
    alignItems: "center",
    justifyContent: "center",
  },
  image: {
    marginBottom: 80,
    width :200,
    height:200
  },
  inputView: {
    backgroundColor: "white",
    borderColor:"rgb(163, 60, 60)",
    borderWidth: 3.5,
    borderRadius: 5,
    width: "85%",
    height: 50,
    marginBottom: 20,
    alignItems: "center",
    textAlign:"left",
  },
  TextInput: {
    fontSize:20,
    width:"100%",
    height: 50,
    flex: 1,
    padding:0,
    marginLeft: 10,
    textAlign:"left",
    color:"rgb(100, 128, 128)",
  },
  forgot_button: {
    height: 30,
    marginTop :20,
    marginBottom: 0,
    fontSize:25,
    color:"rgb(100, 128, 128)",
  },
  loginBtn: {
    width: "85%",
    borderRadius: 5,
    height: 80,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 40,
    fontSize:50,
    Size:50,
    backgroundColor: "rgb(163, 60, 60)",
  },
  loginText :{
    fontSize :30,
    lineHeight:2,
    fontStyle:"normal"
  },plustext :{
    color:"blue",
    fontSize:50,
    marginBottom:-90,
  }
});