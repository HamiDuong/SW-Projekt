import React from 'react';
import Navigation from './Components/Navigator';
//import Calendar from './Components/Calendar';
import MyWorkTime from './Components/Pages/MyWorkTime';
import Navigator from './Components/Navigator';
import { ThemeProvider } from '@mui/material/styles';
import Theme from './Theme';
import { CssBaseline } from '@mui/material';
import Calculator from './Components/Pages/Example'

class App extends React.Component {
  render() {
    return (
      <ThemeProvider theme={Theme}>
        <CssBaseline />
        <div>
          <Navigator></Navigator>
          <Calculator />
          <MyWorkTime />
        </div>
      </ThemeProvider>
    )
  }
}

export default App;

