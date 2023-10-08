import Meta from '@/components/Meta';
import { FlexBox, FullSizeCenteredFlexBox } from '@/components/styled';
import useOrientation from '@/hooks/useOrientation';
import Button from '@mui/material/Button';
import S4logo from './logos/S4.svg';
import { Image, Text, Body, GetStartedButton } from './styled';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import { useNavigate } from 'react-router-dom';

function Welcome() {
  const isPortrait = useOrientation();

  const width = isPortrait ? '40%' : '30%';
  const height = isPortrait ? '30%' : '40%';

  // Initialize the navigate function from React Router
  const navigate = useNavigate();

  // Define a function to handle button click and navigate to the desired route
  const handleButtonClick = () => {
    navigate('./QOLScripts');
  };

  return (
    <>
      <Meta title="Welcome" />
      {/* <FullSizeCenteredFlexBox flexDirection={isPortrait ? 'column' : 'row'}>
        <Image alt="Shift4" src={S4logo} sx={{ width, height }} />
      </FullSizeCenteredFlexBox> */}
      <FlexBox flexDirection="column" alignItems="center" justifyContent="center">
        <Text>
          <Typography variant="h2">Welcome to the VenueNext QOL Tools!</Typography>
        </Text>
        <Divider flexItem />
        <Body>
          <Typography variant="h4">This app can be used to run specific scripts, making JSON requests and responses much easier to format. Links out to each of the ecosystems are also provided in the header. Click the button below to get started.</Typography>
        </Body>
        {/* Use the Material-UI Button component with the onClick handler */}
        <GetStartedButton onClick={handleButtonClick} color='primary' 
          sx={{ 
            marginTop: '64px', 
            borderRadius: '5px', 
            padding: '16px 32px',
            fontSize: '18px' 
            }}>
              GET STARTED!
        </GetStartedButton>
      </FlexBox>
    </>
  );
}

export default Welcome;
