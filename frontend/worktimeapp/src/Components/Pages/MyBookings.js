import React, {Component} from 'react';
import { RadioGroup, Radio, FormControlLabel, FormControl, FormLabel } from '@mui/material';
import MyBookingsEntry from '../MyBookingsEntry';
import 

class MyBookings extends Component{
    constructor(props){
        super(props);
        this.state = {
            bookings: [],
            loadingInProgress: false,
            error: null,
        }
    }

    getBookings = () => {
        let data = this.props.googleId;
    }

    render(){
        return(
            <div>
                <div>
                    <FormControl>
                        <FormControlLabel>Welche Buchungen anzeigen</FormControlLabel>
                        <RadioGroup
                            row
                            name="booking-selection"
                            value={value}
                            onChange={handleChange}
                        >
                            <FormControlLabel value="all" control={<Radio />} label="Alle anzeigen" />
                            <FormControlLabel value="interval" control={<Radio />} label="Nur Intervallbuchungen" />
                            <FormControlLabel value="event" control={<Radio />} label="Nur Eventbuchungen" />
                        </RadioGroup>  
                    </FormControl>
                </div>
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
            </div>
        );
    }
}