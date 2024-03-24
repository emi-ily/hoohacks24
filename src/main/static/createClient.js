import { createClient } from "@propelauth/javascript";

const authClient = createClient({
    // The base URL where your authentication pages are hosted. You can find this under the Frontend Integration section for your project.
    authUrl: "https://59223397842.propelauthtest.com",
    // If true, periodically refresh the access token in the background. This helps ensure you always have a valid token ready to go. Default true.
    enableBackgroundTokenRefresh: true,
});

const authInfo = await authClient.getAuthenticationInfoOrNull()
if (authInfo) {
    console.log("User is logged in as", authInfo.user.email)
} else {
    console.log("User is not logged in")
}
