//Gerüst für firebaseConfig ist aufgebaut
import { initializeApp } from 'firebase/app';
import { getAuth } from "firebase/auth";



const firebaseConfig = {
  
    apiKey: "AIzaSyAfz5B-AK5xLjBhRUfTvBKF58GpIfAHa78",
    authDomain: "worktimeapp-2f279.firebaseapp.com",
    projectId: "worktimeapp-2f279",
    storageBucket: "worktimeapp-2f279.appspot.com",
    messagingSenderId:  "1081715084225",
    appId: "1:1081715084225:web:19f723cc69c1c2f0fc3d40"
};
 
const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
