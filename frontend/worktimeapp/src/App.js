import React from 'react';
import Navigation from './Components/Navigator';
//import Calendar from './Components/Calendar';
import MyWorkTime from './Components/Pages/MyWorkTime';
import Navigator from './Components/Navigator';
import { ThemeProvider } from '@mui/material/styles';
import Theme from './Theme';
import { CssBaseline } from '@mui/material';
import ProjectTimeOverview from './Components/Pages/Example'
import BasicSelect from './Components/dropdown';

class App extends React.Component {
  render() {
    return (
      <ThemeProvider theme={Theme}>
        <CssBaseline />
        <div>
          <Navigator></Navigator>
          <ProjectTimeOverview />


        </div>
      </ThemeProvider>
    )
  }
}

export default App;

