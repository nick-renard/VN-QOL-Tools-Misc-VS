import isMobile from '@/utils/is-mobile';

import type { Notifications } from './types';

const title = 'VenueNext QOL Tools';

const author_name = 'Nick Renard';

const repository = '';

const messages = {
  app: {
    crash: {
      title: 'Oooops... Sorry, I guess something went wrong...',
      options: {
        email: `Contact ${author_name} for some help.`,
        reset: 'Press here to reset the application',
      },
    },
  },
  loader: {
    fail: 'Hmmmmm, there is something wrong with this component loading process... Maybe trying later would be the best idea',
  },
  images: {
    failed: 'something went wrong during image loading :(',
  },
  404: 'Hey bro? What are you looking for?',
};

const dateFormat = 'MMMM DD, YYYY';

const notifications: Notifications = {
  options: {
    anchorOrigin: {
      vertical: 'bottom',
      horizontal: 'left',
    },
    autoHideDuration: 6000,
  },
  maxSnack: isMobile ? 3 : 4,
};

const loader = {
  // no more blinking in your app
  delay: 300, // if your asynchronous process is finished during 300 milliseconds you will not see the loader at all
  minimumLoading: 700, // but if it appears, it will stay for at least 700 milliseconds
};

const defaultMetaTags = {
  image: '/cover.png',
  description: 'Starter kit for modern web applications',
};
const giphy404 = 'https://giphy.com/embed/Qr6IxCV9ZUe4jnjSIi'

const scriptRows = [
    { id: 1, scriptName: 'Braintree to Shift4 Processing', description: 'Takes the stands index response, applies the Merchant to all stands, and removes all Braintree values', run: "" },
    { id: 2, scriptName: 'Levy Suites Token Application', description: 'Applies the merchant token directly to Levy Suites stands', run: "" },
    // { id: 3, scriptName: 'Order UUIDs from Order Index', description: 'This script...', run: "" },
  ];

export {
  loader,
  notifications,
  dateFormat,
  messages,
  repository,
  author_name,
  title,
  defaultMetaTags,
  giphy404,
  scriptRows,
};
