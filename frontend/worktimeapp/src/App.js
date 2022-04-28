import React from 'react';
import Navigation from './Components/Navigator';
//import Calendar from './Components/Calendar';
import MyBookings from './Components/Pages/MyBookings';
import { ThemeProvider} from  '@mui/material/styles';
import Theme from './Theme';
import { CssBaseline } from '@mui/material';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';
import NavBar from './Components/NavBar';
import Test from './Components/Test'
import MyProfile from './Components/MyProfile';
import CreateProject from './Components/CreateProject';
import MyWorkTime from './Components/MyWorkTime';



class App extends React.Component {
 render(){
   return(
    <ThemeProvider theme={Theme}>
      <CssBaseline/>
      <div>
        {/* <MyBookings></MyBookings> */}
        {/* <Navigation/> */}
      <Router>
        <NavBar/>
        <Routes>
          <Route path='/myprofile' exact element={<MyProfile/>}/>
          <Route path='/mybookings' exact element={<MyBookings/>}/>
          <Route path='/createproject' exact element={<CreateProject/>}/>
          <Route path='/myworktime' exact element={<MyWorkTime/>}/>
          <Route path='/test' element={<Test/>}/>
        </Routes>
      </Router>
     </div>         
     </ThemeProvider>    
   ) 
 }
}
 
export default App;

