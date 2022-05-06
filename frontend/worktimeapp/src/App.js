import React from 'react';
import MyBookings from './Components/Pages/MyBookings';
import { ThemeProvider} from  '@mui/material/styles';
import Theme from './Theme';
import { CssBaseline } from '@mui/material';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';
import NavBar from './Components/NavBar';
import MyProfile from './Components/MyProfile';
import CreateProject from './Components/CreateProject';
import MyWorkTime from './Components/MyWorkTime';
import TimeIntervalBookings from './Components/TimeIntervalBookings';
import EventBookings from './Components/EventBookings';
import Bookings from './Components/Bookings';
import MyProjects from './Components/MyProjects';


class App extends React.Component {
 render(){
   return(
    <ThemeProvider theme={Theme}>
      <CssBaseline/>
      <div>
      <Router>
        {/* Der Router und der Navigationleiste wird in diesem Abschnitt ausgeführt.
         */}
        <NavBar/>
        <Routes>
          <Route path='/myprofile' exact element={<MyProfile/>}/>
          <Route path='/mybookings' exact element={<MyBookings/>}/>
          <Route path='/myprojects' exact element={<MyProjects/>}/>
          <Route path='/timeintervalbookings' exact element={<TimeIntervalBookings/>}/>
          <Route path='/eventbookings' exact element={<EventBookings/>}/>
          <Route path='/createproject' exact element={<CreateProject/>}/>
          <Route path='/myworktime' exact element={<MyWorkTime/>}/>
          
        </Routes>
      </Router>
     </div>         
     </ThemeProvider>    
   ) 
 }
}
 
export default App;

