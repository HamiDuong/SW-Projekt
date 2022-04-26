// import React, { useState } from "react";
// import SnoozeIcon from '@mui/icons-material/Snooze';
// import { IconButton } from "@mui/material";
// import { InputAdornment } from "@mui/material";
// import { DateTimePicker, KeyboardDateTimePicker } from "@mui/x-date-pickers";
 
// function Calendar(props) {
//  const [clearedDate, handleClearedDateChange] = useState(null);
//  const [selectedDate, handleDateChange] = useState(new Date("2019-01-01T18:54"));
 
//  return (
//    <>
//      <DateTimePicker
//        autoOk
//        disableFuture
//        hideTabs
//        ampm={false}
//        value={selectedDate}
//        onChange={handleDateChange}
//        allowKeyboardControl={false}
//        minDate={new Date("2022-01-01")}
//        helperText="Hardcoded helper text"
//        leftArrowButtonProps={{ "aria-label": "Prev month" }}
//        rightArrowButtonProps={{ "aria-label": "Next month" }}
//        rightArrowIcon={<SnoozeIcon />}
//        InputProps={{
//          endAdornment: (
//            <InputAdornment position="end">
//              <IconButton>
  
//              </IconButton>
//            </InputAdornment>
//          ),
//        }}
//      />
 
//      {/* <KeyboardDateTimePicker
//        value={selectedDate}
//        onChange={handleDateChange}
//        label="Keyboard with error handler"
//        onError={console.log}
//        minDate={new Date("2018-01-01T00:00")}
//        format="yyyy/MM/dd hh:mm a"
//      /> */}
 
//      <DateTimePicker
//        clearable
//        value={clearedDate}
//        onChange={handleClearedDateChange}
//        helperText="Clear Initial State"
//      />
//    </>
//  );
// }
 
// export default Calendar;

//Das was Herr Kunz gezeigt hat
import * as React from 'react';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';

export default function Calendar() {
  return (
    <Stack component="form" noValidate spacing={3}>
      
      <TextField
        id="datetime-local"
        label="Calendar"
        type="datetime-local"
        defaultValue="2022-01-01T00:00"
        sx={{ width: 250 }}
        InputLabelProps={{
          shrink: true,
        }}
      />
    </Stack>
  );
}

