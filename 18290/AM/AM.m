fs = 22050;                    % sampling rate
Ts = 1/fs;                     % sampling period
Tmax = 2.0;                    % signal duration
t = [0:Ts:Tmax];               % time vector

x = 0.4*cos(2*pi*198*t) + 0.4*cos(2*pi*202*t);

disp('Sum of two sinusoids');

plot(t,x);
axis([0 0.5 -1 1])
xlabel('Time (seconds)');
ylabel('x');

soundsc(x,fs)
wavwrite(x, fs, 'sum.wav')

disp('paused ... multiplication of two sinusoids next');
pause

x = 0.8*cos(2*pi*200*t).*cos(2*pi*2*t);

plot(t,x);
axis([0 0.5 -1 1])
xlabel('Time (seconds)');
ylabel('x');

soundsc(x,fs)
wavwrite(x, fs, 'mult.wav')

disp('paused ... AM next');
pause

x = 0.1*(5 + 2*cos(2*pi*30*t)).*cos(2*pi*200*t);

plot(t,x);
axis([0 0.5 -1 1])
xlabel('Time (seconds)');
ylabel('x');

soundsc(x,fs)
wavwrite(x, fs, 'AM.wav')