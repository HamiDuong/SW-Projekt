import React from 'react';
import MyBookings from './Components/Pages/MyBookings';
import { ThemeProvider } from '@mui/material/styles';
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
import MyProjectsTest from './Components/MyProjectsTest';
import ProjectTimeOverview from './Components/Pages/Example'
import IndividualTime from './Components/Pages/IndividualTimes';
import IndividualTimeEntry from './Components/Pages/IndividualTimeEntry';
import ProjectSelection from './Components/Pages/ProjectSelections';


class App extends React.Component {
  render() {
    return (
      <ThemeProvider theme={Theme}>
        <CssBaseline />
        <div>
          <Router>
            {/* Der Router und der Navigationleiste wird in diesem Abschnitt ausgeführt.
         */}
            <NavBar />
            <Routes>
              <Route path='/myprofile' exact element={<MyProfile />} />
              <Route path='/Individual' exact element={<IndividualTime />} />
              <Route path='/Example' exact element={<ProjectTimeOverview />} />
              <Route path='/mybookings' exact element={<MyBookings />} />
              <Route path='/myprojects' exact element={<MyProjects />} />
              <Route path='/timeintervalbookings' exact element={<TimeIntervalBookings />} />
              <Route path='/eventbookings' exact element={<EventBookings />} />
              <Route path='/createproject' exact element={<CreateProject />} />
              <Route path='/myworktime' exact element={<MyWorkTime />} />
              <Route path='/myprojectstest' exact element={<MyProjectsTest />} />
              <Route path='/IndividualEntry' exact element={<IndividualTimeEntry />} />
              <Route path='/SelectionProjects' exact element={<ProjectSelection />} />

            </Routes>
          </Router>
        </div>
      </ThemeProvider>
    )
  }
}

export default App;