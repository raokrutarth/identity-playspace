# Backend Design and Resources

TODO - explain main building blocks and maintain resources.

## Authn & Authz Notes

- Oauth2 was built to combat the lack of secrecy the comes in with mobile apps.
- Oauth1 assumed client ID and client secret would be kept private.
- Authn = prove user's identity.
- Authz = what the user/service has access to.
- Access tokens.
  - Access tokens are used by clients to make requests to an API.
  - Grant types are the mechanism through which an app will get the access token.
    - Several oauth grants exist. Newer is generally more secure.
  - Auth code grant (most common grant type).
    - client app is redirected to the IDP login page.
    - The idp redirects the client back to the server's app with a code in the URL.
    - the client then uses this code to get an access token.
    - A refresh token is also provided so new access tokens can be obtained without the login page.
    - Auth code grant + PKCE is the most secure.
    - token expiry times.
      - Access tokens should be short lived since they are on the wire most of the time and can be leaked more easily.
      - JWT access tokens also hold user information that my go out of date over time.
    - replay(s) of refresh tokens should be blocked?
    - PKCE with client secret.
      - client app generates a hash of a secret and gives the IDP.
      - Then, client app gets redirected to the IDP for login.
      - The code the IDP generates takes the hashed secret into account.
      - When the client app makes a request to the server for an access token, it sends the raw secret to prove the client app got the code from the IDP.

## Resources

### Pending

- Resources, top tools list & talks <https://github.com/kdeldycke/awesome-iam>
  - Spotify authn design <https://shopify.engineering/implement-secure-central-authentication-service-six-steps>
  - Buzzfeed SSO diagram <https://increment.com/security/open-sourcing-buzzfeeds-single-sign-on-process/>
- Auth servers/IDPs
  - Keycloak <https://www.keycloak.org/>
    - <https://github.com/thomasdarimont/awesome-keycloak>
    - sp feature list demo <https://www.youtube.com/watch?v=duawSV69LDI>
    - YT playlist with features <https://www.youtube.com/playlist?list=PLPZal7ksxNs0mgScrJxrggEayV-TPZ9sA>
    - docker quickstart <https://www.keycloak.org/getting-started/getting-started-docker>
    - Flask plus keycloak <https://github.com/houmie/sso>
    - User role mapping <https://www.thomasvitale.com/keycloak-configuration-authentication-authorisation/>
    - Grant type config <https://www.thomasvitale.com/keycloak-authentication-flow-sso-client/>
    - Custom theme: <https://www.keycloak.org/docs/latest/server_development/#theme-types>
    - general keycloak admin py lib <https://github.com/marcospereirampj/python-keycloak>
    - keycloak dc and gw with py <https://github.com/xyder/example-krakend-keycloak/blob/master/docker-compose.yml>
      - explained: <https://www.krakend.io/docs/authorization/keycloak/>
    - Secure Frontend (React.js) and Backend (Node.js/Express Rest API) with Keycloak
      - <https://medium.com/devops-dudes/secure-front-end-react-js-and-back-end-node-js-express-rest-api-with-keycloak-daf159f0a94e>
  - authentik (feature rich) <https://github.com/goauthentik/authentik>
    - python code sample <https://github.com/CodeMasterr69/flask_authentik/blob/main/example.py>
  - auth server with good reverse proxy integration: <https://github.com/authelia/authelia>
    - Has docker deployment docs.
    - Works with modern reverse proxies (e.g. nginx)
  - lightweight server with /login endpoint <https://github.com/tarent/loginsrv>
    - good intro docs
  - Okta
    - SSO API <https://developer.okta.com/docs/guides/build-sso-integration/openidconnect/main/>
  - WSO2
    - <https://is.docs.wso2.com/en/latest/get-started/quick-start-guide/>
    - Director of company authored multiple B2B authn books.
  - hydra
    - <https://www.ory.sh/docs/hydra/5min-tutorial>
    - <https://www.ory.sh/docs/kratos/quickstart>
  - Enterprise multi-cloud sol <https://www.boundaryproject.io/>
    - Use case not clear.
  - FusionAuth
    - <https://github.com/FusionAuth/fusionauth-example-python-flask/blob/master/app/views.py>
  - <https://gluu.org/>
  - <https://auth0.com/pricing>
    - Limited free tier functionality.
  - <https://aws.amazon.com/cognito/>
  - <https://cloud.google.com/identity-platform/pricing>
- SDK based auth: <https://supertokens.com/docs/thirdpartyemailpassword/quick-setup/video-tutorial>
- Authorization Code & Client Credentials diagrams sp:
  - <https://fusionauth.io/learn/expert-advice/oauth/modern-guide-to-oauth>
- Social logins with Flask <https://testdriven.io/blog/flask-social-auth/>
- Oauth py server demo with tokens in UI to learn
  - <https://github.com/MichaelVL/oidc-oauth2-workshop>
- k8s basic artifacts:
  - <https://github.com/microsoft/cookiecutter-spacy-fastapi/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/manifests/service.yml>
- FastAPI
  - <https://fastapi-keycloak.code-specialist.com/> keycloak library sp.
  - <https://github.com/Buuntu/fastapi-react>
  - fastapi plugin <https://fastapi-crudrouter.awtkns.com/dependencies>
  - <https://github.com/Madpilot0/FastAPI-Auth>
  - Multiple DBs + auth + Jenkins <https://github.com/scionoftech/FastAPI-Full-Stack-Samples>
  - User Management library <https://fastapi-users.github.io/fastapi-users/>
  - Setting cookie: <https://github.com/hkiang01/fastapi-keycloak-oidc-auth/blob/master/app/main.py>
  - starlett middleware and context:
    - <https://github.com/tomwojcik/starlette-context>
- JWT live playground API <https://github.com/dwyl/learn-json-web-tokens>
- quick flask jwt auth <https://stribny.name/blog/2018/10/flask-api-quickstart-application-with-json-web-tokens-sqlalchemy-and-pytest/>
- Very basic authorize and call back endpoint example <https://github.com/tanveer941/Oauth2.0-demo/blob/master/app.py>
- Oauth best practices RFC <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-16>

### Done

- <https://changelog.com/podcast/456>
  - 29m
  - 48m
- oauth+pkce intro <https://www.youtube.com/watch?v=HhwUMESAddM>
- FusionAuth <https://realpython.com/podcasts/rpp/99/?__s=d114gfvtjkkk4ut5uecn>
  - 7m auth providers alternatives.
  - Advantages of 3rd party solution.
