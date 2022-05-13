import React, {Component} from 'react';
import { RadioGroup, Radio, FormControlLabel, FormControl, FormLabel } from '@mui/material';
import MyBookingsEntry from '../MyBookingsEntry'

class MyBookings extends Component {
    constructor(props){
        super(props);
        this.state = {
            bookings: [],
            loadingInProgress: false,
            error: null,
        }
    }

    state = {  }
    render(){
        const {bookings, loadingInProgress} = this.state;
        return(
            <div>
                <p>Hier steht etwas</p>
                <div>
                    <input></input>
                    <input type="text" id="startdatum"/>
                    <input type="text" id="enddatum"/>
                    <select id="filter">
                        <option value="work">Arbeiten</option>
                        <option value="flex day">Gleittag</option>
                        <option value="illness">Krank</option>
                        <option value="vacation">Urlaub</option>
                        <option value="break">Pause</option>
                        <option value="project work">Projektarbeit</option>
                    </select>
                </div>
                <button onClick={console.log(this.getTypeOfBooking)}>Knopf</button>
                <div>
                </div>
            </div>
        );
    }
}
 
export default MyBookings;