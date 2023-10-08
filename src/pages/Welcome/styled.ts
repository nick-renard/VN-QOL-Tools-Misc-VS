import { styled } from '@mui/system';

const Image = styled('img')({
  width: '10%',
  height: '10%',
  margin: 4,
  // position to top center
  position: 'absolute',
  top: '20%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
});


const Text = styled('p')({
  // position to top center
  position: 'absolute',
  marginTop: '5%',
  width: 'fit-content',
  top: '20%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  textAlign: 'center',
  fontWeight: 'bolder',
});

const Body = styled('body')({
  // position to top center
  position: 'absolute',
  marginTop: '5%',
  width: '75%',
  height: 'fit-content',
  top: '40%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  textAlign: 'center',
  // not bold
  fontWeight: 'lighter',
});

const GetStartedButton = styled('button')({
  // Position the button below the text
  position: 'absolute',
  top: '65%', // Adjust the top value as needed for vertical positioning
  left: '50%',
  transform: 'translateX(-50%)', // Center horizontally
  background: 'blue', // Blue background color
  color: 'white', // White text color
  padding: '10px 20px', // Padding for the button
  border: 'none', // Remove button border
  cursor: 'pointer', // Add pointer cursor on hover
  fontWeight: 'bold', // Bold text
});

export { Image, Text, Body, GetStartedButton };