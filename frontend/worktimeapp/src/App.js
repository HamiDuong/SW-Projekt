import React from 'react';
import Navigation from './Components/Navigator';
//import Calendar from './Components/Calendar';
import MyBookings from './Components/Pages/MyBookings';
import { ThemeProvider} from  '@mui/material/styles';
import Theme from './Theme';
import { CssBaseline } from '@mui/material';
 
class App extends React.Component {
 render(){
   return(
    <ThemeProvider theme={Theme}>
      <CssBaseline/>
      <div>
        <MyBookings></MyBookings>
     </div>         
     </ThemeProvider>    
   )
 }
}
 
export default App;

