export const environment = {
  production: true,
  auth: {
    clientID: 'G9F4Z04OhnG4O3i9pty3k9Y0yCieogDW',
    domain: 'dev--vi0q1gg.auth0.com', // e.g., you.auth0.com
    audience: 'http://djangoangularapi',
    auth0RedirectUri: 'http://localhost:4200/', // URL to return to after auth0 login
    auth0ReturnTo: 'http://localhost:4200/', // URL to return to after auth0 logout
    scope: 'openid profile'
  },
};