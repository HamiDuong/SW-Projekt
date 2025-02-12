import React from 'react';
import MyBookings from './Components/Pages/MyBookings';
import { ThemeProvider } from '@mui/material/styles';
import Theme from './Theme';
import { CssBaseline } from '@mui/material';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';
import NavBar from './Components/NavBar';
import MyProfile from './Components/MyProfile';
import CreateProject from './Components/Pages/CreateProjectMain';
import TimeIntervalBookings from './Components/TimeIntervalBookings';
import EventBookings from './Components/EventBookings';
import MyProjects from './Components/MyProjects';
import ProjectWorkTimeOverviewAdmin from './Components/Pages/ProjectWorkTimeOverviewAdmin'
import Login from './Components/Login';
import { GoogleAuthProvider, signInWithRedirect, onAuthStateChanged } from "firebase/auth";
import { auth } from './firebaseConfig.js';
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import WorkTimeAppAPI from './API/WorkTimeAppAPI';
import IndividualSelection from './Components/Pages/ProjectWorkTimeOverview';
import WelcomePage from './Components/WelcomePage';
class App extends React.Component {
  constructor(props) {
    super(props);
    // Init an empty state
    this.state = {
      currentUser: null,
      appError: null,
      authError: null,
      userId: null,
      workTimeAccountId: null,
    };
  }
  handleSignIn = () => {
    const provider = new GoogleAuthProvider();
    signInWithRedirect(auth, provider)
      .then((re) => {
        console.log("test")
      })
  }
  handleAuthStateChange = user => {
    if (user) {

      // The user is signed in
      user.getIdToken().then(token => {
        // Add the token to the browser's cookies. The server will then be
        // able to verify the token against the API.
        // SECURITY NOTE: As cookies can easily be modified, only put the
        // token (which is verified server-side) in a cookie; do not add other
        // user information.
        document.cookie = `token=${token};path=/`;
        const uid = user.uid;
        console.log('IM HEEERRREEE')
        console.log(uid)
        // Set the user not before the token arrived
        this.setState({
          currentUser: user,
          authError: null,
        }, this.getUserId(user.uid)
        );
      }).catch(e => {
        this.setState({
          authError: e,
        });
      });
    } else {
      // User has logged out, so clear the id token
      document.cookie = 'token=;path=/';
      // Set the logged out user to null
      this.setState({
        currentUser: null,
      });
    }
  }
  getUserId = (id) => {
    WorkTimeAppAPI.getAPI().getUserByGoogleUserId(id).then(userBO => {
      this.setState({
        userId: userBO[0].getID()
      }, function () {
        console.log("UserId", this.state.userId)
        this.getWorkTimeAccountId(userBO[0].getID())
      }
      )
    })
  }
  getWorkTimeAccountId = (id) => {
    WorkTimeAppAPI.getAPI().getWorkTimeAccountByUserId(id).then(accountBO => {
      this.setState({
        workTimeAccountId: accountBO[0].getID()
      }, function () {
        console.log("WorktimeAccountId", this.state.workTimeAccountId)
      })
    })
  }
  componentDidMount() {
    onAuthStateChanged(auth, this.handleAuthStateChange)
  }
  render() {
    return (
      <ThemeProvider theme={Theme}>
        
        <CssBaseline />
        <div>
          {this.state.currentUser && this.state.userId ?

            <Router>
              {/* Der Router und der Navigationleiste wird in diesem Abschnitt ausgeführt.*/}
              <NavBar user={this.state.currentUser} />
              <Routes>
                <Route path='/' exact element={<WelcomePage/>}></Route>
                <Route path='/myprofile' exact element={<MyProfile user={this.state.currentUser} workTimeAccount={this.state.workTimeAccountId} />} />
                <Route path='/mybookings' exact element={<MyBookings userId={this.state.userId} workTimeAccountId={this.state.workTimeAccountId} />} />
                <Route path='/myprojects' exact element={<MyProjects userId={this.state.userId} workTimeAccountId={this.state.workTimeAccountId} />} />
                <Route path='/timeintervalbookings' exact element={<TimeIntervalBookings userId={this.state.userId} workTimeAccountId={this.state.workTimeAccountId} />} />
                <Route path='/eventbookings' exact element={<EventBookings userId={this.state.userId} workTimeAccountId={this.state.workTimeAccountId} />} />
                <Route path='/createprojectmain' exact element={<CreateProject userId={this.state.userId} workTimeAccountId={this.state.workTimeAccountId} user={this.state.currentUser} />} />
                <Route path='/adminoverview' exact element={<ProjectWorkTimeOverviewAdmin userId={this.state.userId} workTimeAccountId={this.state.workTimeAccountId} />} />
                <Route path='/individualEntry' exact element={<IndividualSelection userId={this.state.userId} workTimeAccountId={this.state.workTimeAccountId} />} />
              </Routes>
            </Router>
            :
            <Login onLogIn={this.handleSignIn} />
          }
        </div>
      </ThemeProvider>
    )
  }
}
export default App;