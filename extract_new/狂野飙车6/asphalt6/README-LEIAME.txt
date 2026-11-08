ASPHALT 6: ADRENALINE by Mega & NextOS
Only version 1.3.3 of A6 have been tested

WARNING: At least 2 GB of storage is required to install and extract files for this port. You can delete the apk and the original data folder from the game later.

INSTALLATION:
Put the APK and extracted cache together in asphalt6/data/. The APK must be directly inside data/, outside the cache subfolder. Prepared installations keep working without the APK.
1: Copy asphalt6.sh and asphalt6 folder to "/ports" folder on your device
2: Add your own copy of Asphalt 6: Adrenaline APK v1.3.3 directly inside "/asphalt6/data".
3: Add your own copy of Asphalt 6: Adrenaline data folder from v1.3.3 inside "/asphalt6/data".
4: If you set up all files correctly, the first boot on the game will extract all files needed for the execution.
5: It will also install a fix for a specific crash (located at "/asphalt6/tools" folder), don't skip any of this, it should prompt around 4 screens - game extraction, confirmation, vehicle fix patch and fix patch confirmation. Again, this will happen only on the first boot of the game.

6: (OPTIONAL) You can delete the .apk and the original data files folder to free up space. OBSERVATION: You can delete the data folder INSIDE "asphalt6/data", which probably is named "asphalt6", do not delete the port data folder itself. Maybe in the future I'll implement a option on first boot to auto-delete unnecessary files. However, I recommend keeping it if possible in case a file corruption happens, so the port can be repaired.

FULL SAVE GAME (OPTIONAL):
Asphalt saves are stored inside the extracted cache folder as "profile1.bak" and "profile1.sav".
Extracted cache folder: "gamefiles/sdcard/gameloft/games/GloftA6HP"
Inside "tools" folder you can find a 100% save data, with:
   ALL CARS UNLOCKED
   ALL TRACKS UNLOCKED
   A LOT OF MONEY
   100% COMPLETION ON CAMPAIGN

To install the 100% save, copy both "profile1.bak" and "profile1.sav" from "tools/Full Save Data" folder to the extracted cache folder. Replace the previous files with the full save ones.

CONTROLS:
  D-pad / left stick: menu navigation and left/right vehicle steering.
  Right stick: pointer. R3: click at pointer position.
  A: native confirmation and continue on track intros/tutorial overlays. Accelerate the vehicle.
  B: native cancel/return.
     OBSERVATION: On some devices, the functions of the A and B buttons will be reversed.
  L1/L2: brake.
  R1/R2: nitro.
  START (during gameplay): pause.
  Hold START+SELECT, in either order: exit to the ports menu.
  The GO-Super Gamepad (used on some R36S clones) mapping now includes buttons 12-15.

SETTINGS:
Open asphalt6/config.ini with a text editor.
AUTO_ACCELERATION = ON (default): automatically accelerate in races.
AUTO_ACCELERATION = OFF: use the existing manual accelerator button.
The setting is read silently once at each game launch. Restart after editing.
Brake, steering, nitro, menu confirmation and R3 drag are unchanged.
Missing/invalid settings use ON. The chosen value appears only in the log.

The engine is locked to its physical keyboard/gamepad control mode (type 4).
Selecting phone schemes A/B/C/D cannot change that effective mode; the
settings entry itself is still visible. Touch driving controls are hidden
in the race HUD; upper race information is retained.

ISSUES AND TROUBLESHOOTING:
Only the three most recent game logs are retained. Automatic per-launch save backups are disabled.
On muOS, the launcher temporarily stops active PipeWire/WirePlumber services for direct ALSA audio and restores them on exit. Volume keys use the existing hardware volume level.

Any issues regarding crashes, visual, music or controls will generate a log at /logs folder.
Make sure to send the latest log files from that folder on NextOS Discord chat related to Asphalt 6 port.

CREDITS:
Compiled and adjusted by Mega from NextOS Discord
muOS audio diagnosis and original adaptation: Mikhail/Crescent
Base and framework: NextOS — https://github.com/NextOs-Ports





----- PORTUGUESE INFO

ASPHALT 6: ADRENALINE by Mega & NextOS
Apenas a versão 1.3.3 do A6 foi testada

AVISO: São necessários pelo menos 2 GB de espaço de armazenamento para instalar e extrair os arquivos do jogo. Você pode apagar o arquivo APK e a pasta de dados original do jogo mais tarde.

INSTALAÇÃO:
Coloque o APK e o cache extraído juntos em asphalt6/data/. O APK deve ficar diretamente em data/, fora da subpasta do cache. Instalações já preparadas continuam funcionando sem o APK.
1: Copie o arquivo asphalt6.sh e a pasta asphalt6 para a pasta «/ports» no seu dispositivo
2: Adicione a sua própria cópia do APK do Asphalt 6: Adrenaline v1.3.3 diretamente na pasta «/asphalt6/data».
3: Adicione a sua própria cópia da pasta de dados do Asphalt 6: Adrenaline da versão 1.3.3 dentro de «/asphalt6/data».
4: Se tiver configurado todos os arquivos corretamente, a primeira inicialização do jogo irá extrair todos os arquivos necessários para a execução.
5: Tambem vai ocorrer a instalação de uma correção para uma falha específica (localizada na pasta «/asphalt6/tools»); não ignore nenhuma destas etapas; deverá aparecer cerca de 4 telas: extração do jogo, confirmação, patch de correção dos veículos e confirmação do patch de correção. Isto só acontecerá na primeira vez que você iniciar o jogo.

6: (OPCIONAL) Pode eliminar o arquivo .apk e a pasta original dos arquivos de dados (não a pasta de dados propriamente dita da versão portada, mas sim a pasta "asphalt6" dentro de «/asphalt6/data») para libertar espaço. Talvez no futuro eu implemente uma opção na primeira inicialização para eliminar automaticamente os arquivos desnecessários. Eu recomendo manter caso os arquivos corrompam por algum motivo, para que o port possa ser reparado.

SAVE ZERADO DO JOGO (OPCIONAL):
Os arquivos de gravação do Asphalt são armazenados na pasta de cache extraída como «profile1.bak» e «profile1.sav».
Pasta de cache extraída: «gamefiles/sdcard/gameloft/games/GloftA6HP»
Dentro da pasta «tools» pode encontrar um arquivo de gravação a 100%, com:
   TODOS OS CARROS DESBLOQUEADOS
   TODAS AS PISTAS DESBLOQUEADAS
   MUITO DINHEIRO
   100% DE CONCLUSÃO DA CAMPANHA

Para instalar o save zerado, copie os arquivos «profile1.bak» e «profile1.sav» da pasta «tools/Full Save Data» para a pasta de cache extraída. Substitua os arquivos anteriores pelos arquivos do save zerado.

COMANDOS:
  D-pad / analógico esquerdo: navegação no menu e direção do veículo para a esquerda/direita.
  Analógico direito: ponteiro. R3: clicar na posição do ponteiro.
  A: confirmação nativa e continuar nas introduções da pista/sobreposições do tutorial. Acelerar o veículo.
  B: cancelar/revertê-lo nativo.
     OBSERVAÇÃO: Em alguns dispositivos, as funções dos botões A e B estarão invertidas.
  L1/L2: freio.
  R1/R2: nitro.
  START (durante o jogo): pausar.
  Mantenha pressionado START+SELECT, em qualquer ordem: sair para o menu de portas.
  O mapeamento do GO-Super Gamepad (utilizado em alguns clones do R36S) inclui agora os botões 12-15.

CONFIGURAÇÕES ADICIONAIS:
Abra o arquivo asphalt6/config.ini com um editor de texto.
AUTO_ACCELERATION = ON (predefinição): acelera automaticamente nas corridas.
AUTO_ACCELERATION = OFF: utiliza o botão de aceleração manual existente.
A configuração é lida silenciosamente uma vez em cada inicialização do jogo. Reinicie após a edição.
O freio, a direção, o nitro, a confirmação do menu e o arrastar com R3 permanecem inalterados.
As definições em falta ou inválidas utilizam o valor ON. O valor escolhido aparece apenas no registo.

O motor está bloqueado no seu modo de controlo físico de teclado/gamepad (tipo 4).
A seleção dos esquemas de telemóvel A/B/C/D não altera esse modo efetivo; a
própria entrada de definições continua visível. Os controlos de condução táteis estão ocultos
no HUD da corrida; as informações superiores da corrida são mantidas.

PROBLEMAS E RESOLUÇÃO DE PROBLEMAS:
São mantidos apenas os três logs mais recentes. Os backups automáticos de saves a cada execução foram removidos.
No muOS, o launcher interrompe temporariamente os serviços PipeWire/WirePlumber ativos para usar áudio ALSA direto e os restaura ao sair. Os botões de volume usam o nível atual do aparelho.

Quaisquer problemas relacionados com falhas, gráficos, música ou controlos irão gerar um registo na pasta /logs.
Certifique-se de enviar os arquivos de registo mais recentes dessa pasta no chat do Discord da NextOS relacionado com a versão do Asphalt 6.

CRÉDITOS:
Compilado e ajustado por Mega do Discord do NextOS
Diagnóstico do áudio e adaptação original para muOS: Mikhail/Crescent
Base e estrutura: NextOS — https://github.com/NextOs-Ports




