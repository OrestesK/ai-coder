import "./globals.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-gray-50 text-gray-800">
        <header className="bg-blue-600 text-white p-4">
          <h1 className="text-xl font-bold">Code Feedback</h1>
        </header>
        <main className="p-6">{children}</main>
      </body>
    </html>
  );
}
